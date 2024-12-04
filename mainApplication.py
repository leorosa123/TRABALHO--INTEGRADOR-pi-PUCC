from flask import Flask, request, jsonify, render_template
import psycopg2

# Configuração do Flask
app = Flask(__name__, template_folder='./front-end/view', static_folder='./front-end/confg')

# Função para conectar ao banco de dados
def get_db_connection():
    return psycopg2.connect(
        host='127.0.0.1:3306',
        user='root',
        password='RiCk20052020.com.br',
        database='BancoDeDadosHOPE',
    )

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
        data = request.json
        email = data.get('email')
        senha = data.get('senha')

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

        if user:
            return jsonify({
                "pacienteID": user[0],
                "nomePaciente": user[1],
                "dataNascPaciente": user[2],
                "pacienteCPF": user[3],
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

        # Verifica se o paciente já tem 5 consultas
        cursor.execute("SELECT COUNT(*) FROM consulta WHERE pacienteID = %s", (data['pacienteID'],))
        consulta_count = cursor.fetchone()[0]

        if consulta_count >= 5:
            return jsonify({"error": "Você já atingiu o limite de 5 consultas."}), 400

        # Verifica disponibilidade do horário
        cursor.execute("""
            SELECT * FROM consulta WHERE psicologoID = %s AND dataHoraConsulta = %s
        """, (data['psicologoID'], data['dataHoraConsulta']))
        consulta_existente = cursor.fetchone()

        if consulta_existente:
            return jsonify({"error": "Horário indisponível."}), 400

        # Insere a consulta
        cursor.execute("""
            INSERT INTO consulta (pacienteID, psicologoID, dataHoraConsulta)
            VALUES (%s, %s, %s)
        """, (data['pacienteID'], data['psicologoID'], data['dataHoraConsulta']))
        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Consulta agendada com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Rota para cadastrar novo usuário (POST)
@app.route('/receberDados', methods=['POST'])
def receberDados():
    data = request.json
    campos_necessarios = ['name', 'email', 'pass', 'cpf', 'datanasc']

    if not all(campo in data for campo in campos_necessarios):
        return jsonify({"mensagem": "Dados incompletos."}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT idPaciente FROM pacientes WHERE email = %s OR pacienteCPF = %s", (data['email'], data['cpf']))
        resultado = cursor.fetchone()

        if resultado:
            return jsonify({"mensagem": "E-mail ou CPF já cadastrado."}), 409

        cursor.execute("""
            INSERT INTO pacientes (nomePaciente, email, senha, pacienteCPF, dataNascPaciente)
            VALUES (%s, %s, %s, %s, %s)
        """, (data['name'], data['email'], data['pass'], data['cpf'], data['datanasc']))
        conn.commit()
        return jsonify({"mensagem": "Cadastro realizado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"mensagem": "Erro interno no servidor."}), 500


# Rota para atualizar dados de pacientes (POST)
@app.route('/atualizar', methods=['POST'])
def atualizarDados():
    try:
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE pacientes
            SET nomePaciente = %s, dataNascPaciente = %s, pacienteCPF = %s, email = %s
            WHERE pacienteID = %s
        """, (data['nomePaciente'], data['dataNascPaciente'], data['pacienteCPF'], data['email'], data['pacienteID']))
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

# Para o login
# Verificar se e-mail e senha colocados --> conectar com o querry do banco de dados

# Cadastro
# Verificar as informacoes e se n tem nenhum login com o CPF ou com o email ja feito --> conectar com o banco de dados

# Exibir os psicologos que estao dentro do banco na tela assim que a pagina de agentementos abrir

# Agendamento
# --> cuidado com os horarios na exibicao dos psicologos... eles tem que estar de acordo com as consultas ja marcadas
# --> Uma pessoa nao pode ter mais de 5 consultas
# --> ao clicar no horario --> Trocar para um check verde --> se clicar no check --> consulta marcada