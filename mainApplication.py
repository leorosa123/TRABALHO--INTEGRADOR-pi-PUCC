from flask import Flask, request, jsonify, render_template
from datetime import datetime, timedelta
import pymysql

# Configuração do Flask
app = Flask(__name__, template_folder='./front-end/view', static_folder='./front-end/confg')

# Função para conectar ao banco de dados
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='BancoDeDadosHope',
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
@app.route('/psicologos', methods=['GET', 'POST'])
def psicologos():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DATE_FORMAT(dataHoraConsulta, '%H:%i') AS horaCompleta FROM consultas;
        """)
        horarios = cursor.fetchall()
        conn.close()
    except:
        horarios = []
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT pc.psicologoID, pc.nomePsicologo, pc.especialidade, 
                   pc.descricao, pc.horarioDeAtendimento 
            FROM psicologos pc
        """)
        psicologos = cursor.fetchall()
        conn.close()
        if psicologos:
            # Itera sobre a lista de psicólogos e formata os dados
            resultado = []
            for psico in psicologos:
                # Processa os horários no formato legível
                raw_horarios = psico["horarioDeAtendimento"]
                horarios_formatados = []
                for i in range(0, len(raw_horarios), 8):
                    inicio_hora = raw_horarios[i:i + 2]
                    inicio_minuto = raw_horarios[i + 2:i + 4]
                    termino_hora = raw_horarios[i + 4:i + 6]
                    termino_minuto = raw_horarios[i + 6:i + 8]
                horarios_formatados = []
                inicio = datetime.strptime(f"{inicio_hora}:{inicio_minuto}", "%H:%M")
                termino = datetime.strptime(f"{termino_hora}:{termino_minuto}", "%H:%M")
                atual = inicio

                while atual < termino:
                    if atual.strftime("%H:%M") not in horarios:
                        horarios_formatados.append(atual.strftime("%H:%M"))
                        atual += timedelta(minutes=30)

                resultado.append({
                    "psicologoID": psico["psicologoID"],
                    "nome": psico["nomePsicologo"],
                    "especialidade": psico["especialidade"],
                    "descricao": psico["descricao"],
                    "horarios": horarios_formatados
                })

            return jsonify(resultado)
        else:
            return jsonify({"error": "title"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Rota para agendar consulta (POST)
@app.route('/agendar', methods=['POST'])
def agendar():
    try:
        data = request.json
        print("Dados recebidos para agendamento:", data)
        psicologo_id = data['psicologoID']
        horario = data['dataHoraConsulta']

        conn = get_db_connection()
        cursor = conn.cursor()

        # Verifica se o usuário já tem 5 consultas
        cursor.execute("SELECT COUNT(*) AS total FROM consultas WHERE pacienteID = %s", (data['pacienteID'],))
        consultas = cursor.fetchone()['total']
        if consultas >= 5:
            return jsonify({"error": "Você já atingiu o limite de 5 consultas."}), 400

        # Agenda a consulta
        cursor.execute(
            "INSERT INTO consultas (pacienteID, psicologoID, dataHoraConsulta) VALUES (%s, %s, %s)",
            (data['pacienteID'], psicologo_id, horario)
        )
        conn.commit()
        return jsonify({"mensagem": "Consulta marcada com sucesso!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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

# Exibir os psicologos que estao dentro do banco na tela assim que a pagina de agentementos abrir

# Agendamento
# --> cuidado com os horarios na exibicao dos psicologos... eles tem que estar de acordo com as consultas ja marcadas
# --> Uma pessoa nao pode ter mais de 5 consultas
# --> ao clicar no horario --> Trocar para um check verde --> se clicar no check --> consulta marcada