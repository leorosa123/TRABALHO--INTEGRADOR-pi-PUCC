from flask import Flask, request, jsonify, render_template
import pymysql

# Configuração do Flask
app = Flask(__name__, template_folder='./front-end/view', static_folder='./front-end/confg')

# Função para conectar ao banco de dados
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='RiCk20052020.com.br',
        database='bancodedadoshope',
        cursorclass=pymysql.cursors.DictCursor
    )
    
def test_connection():
    try:
        conn = get_db_connection()
        print("Conexão estabelecida com sucesso!")
        conn.close()
    except Exception as e:
        print("Erro ao conectar ao banco de dados:", e)

if __name__ == "__main__":
    test_connection()

# Rotas para renderizar páginas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.user.html')

@app.route('/login-page')
def login_page():
    return render_template('login.user.html')

@app.route('/informacoes')
def informacoes():
    return render_template('userInformation.html')

@app.route('/agendamento')
def agendamento():
    return render_template('agendamento.html')

# Rota para autenticação de login (POST)
@app.route('/login', methods=['POST'])
def login():
    try:
        # Captura os dados do formulário HTML
        data = request.json
        email = data.get('email')
        senha = data.get('senha')

        # Conecta ao banco de dados
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.pacienteID, p.nomePaciente, p.dataNascPaciente, p.pacienteCPF
            FROM login l
            JOIN pacientes p ON l.userID = p.pacienteID
            WHERE l.email = %s AND l.senha = %s
        """, (email, senha))
        user = cursor.fetchone()
        conn.close()

        # Verifica se o usuário existe
        if user:
            return jsonify({
                "pacienteID": user['pacienteID'],
                "nomePaciente": user['nomePaciente'],
                "dataNascPaciente": user['dataNascPaciente'],
                "pacienteCPF": user['pacienteCPF'],
                "email": email
            })
        else:
            return jsonify({"error": "Credenciais inválidas"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Rota para listar psicólogos (GET)
@app.route('/psicologos', methods=['GET'])
def get_psicologos():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM psicologos")
        psicologos = cursor.fetchall()
        conn.close()
        return jsonify(psicologos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Rota para agendar consulta (POST)
@app.route('/agendar', methods=['POST'])
def agendar():
    try:
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO consulta (pacienteID, psicologoID, dataHoraConsulta)
            VALUES (%s, %s, %s)
        """, (data['pacienteID'], data['psicologoID'], data['dataHoraConsulta']))
        conn.commit()
        conn.close()
        return render_template('index.html')
    except Exception as e:
        return render_template('index.html')

# Rota para cadastrar novo usuário (POST)

@app.route('/receberDados', methods=['POST'])
def receberDados():
    try:
        # Capturando dados enviados via POST
        data = request.form
        name = data.get('name')
        cpf = data.get('cpf')
        datanasc = data.get('datanasc')
        email = data.get('email')
        passw = data.get('pass')

        # Verificação básica para evitar problemas com dados ausentes
        if not all([name, cpf, datanasc, email, passw]):
            return jsonify({"error": "Dados incompletos. Verifique os campos."}), 400

        # Conectando ao banco
        conn = get_db_connection()
        cursor = conn.cursor()
        print("Tentando inserir os valores...")

        # Inserindo os dados na tabela 'pacientes'
        cursor.execute("""
            INSERT INTO pacientes (nomePaciente, pacienteCPF, dataNascPaciente)
            VALUES (%s, %s, %s)
        """, (name, cpf, datanasc))
        
        # Recuperando o pacienteID da última inserção
        paciente_id = cursor.lastrowid

        # Inserindo os dados na tabela 'login'
        cursor.execute("""
            INSERT INTO login (userID, email, senha)
            VALUES (%s, %s, %s)
        """, (paciente_id, email, passw))
        
        # Comitando as mudanças no banco de dados
        conn.commit()
        print("Valor inserido com sucesso.")

        # Fechando a conexão
        conn.close()

        # Retornando uma resposta de sucesso
        return render_template('index.html')
    except Exception as e:
        print("Erro:", e)
        return render_template('index.html')


# Rota para atualizar dados de pacientes (POST)
@app.route('/atualizar', methods=['POST'])
def atualizarDados():
    try:
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE pacientes
            SET nomePaciente = %s, dataNascPaciente = %s, pacienteCPF = %s
            WHERE pacienteID = %s
        """, (data['nomePaciente'], data['dataNascPaciente'], data['pacienteCPF'], data['pacienteID']))

        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Dados atualizados com sucesso!"}), 200
    except Exception as e:
        return jsonify({"mensagem": "Erro ao atualizar os dados.", "erro": str(e)}), 400

# Executar o servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# Se pessoa sem login
# --> Nao pode ir para nenhuma tela alem de login e cadastro

# Assim que a pessoa logar
# Desbloquear o restante das telas
# --> conectar para as informacoes do user e liberar o link de alterar conta no lugar do login e do cadastro
# --> cadastro vira logout e login vira o primeiro nome da pessoa( ao clicar leva para o alterador de informacoes )

# Exibir os psicologos que estao dentro do banco na tela assim que a pagina de agentementos abrir

# Agendamento
# --> cuidado com os horarios na exibicao dos psicologos... eles tem que estar de acordo com as consultas ja marcadas
# --> Uma pessoa nao pode ter mais de 5 consultas
# --> ao clicar no horario --> Trocar para um check verde --> se clicar no check --> consulta marcada