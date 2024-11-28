from flask import Flask, request, jsonify, render_template
import pymysql

app = Flask(__name__, template_folder='./front-end/view')

# Conexão com o banco de dados
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='bancodedadoshope'
    )

# Running main page
@app.route('/')
def index():
    return render_template('index.html')

# Rota para login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    senha = data.get('senha')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT p.pacienteID, p.nomePaciente, p.dataNascPaciente, p.pacienteCPF FROM login l JOIN pacientes p ON login.userID = pacientes.pacienteID WHERE email=%s AND senha=%s", (email, senha))
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

# Rota para listar psicólogos
@app.route('/psicologos', methods=['GET'])
def get_psicologos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM psicologos")
    psicologos = cursor.fetchall()
    conn.close()
    return jsonify(psicologos)

# Rota para agendamento
@app.route('/agendar', methods=['POST'])
def agendar():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO consulta (pacienteID, psicologoID, dataHoraConsulta) VALUES (%s, %s, %s)",
                   (data['pacienteID'], data['psicologoID'], data['dataHoraConsulta']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Consulta agendada com sucesso!"})

# Rota para novo usuario dentro do banco de dados
@app.route('/receberDados', methods = ['POST'])
def receberDados():
    try:
        dados = request.get_json()
        return jsonify({
            "mensagem": "Dados recebidos com sucesso!",
        }), 200
    except Exception as e:
        return jsonify({
            "mensagem": "Erro ao processar os dados.",
            "erro": str(e)
        }), 400
    
    # Pushing receptioneted data to DataBase
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("",
                   (dados['']))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)