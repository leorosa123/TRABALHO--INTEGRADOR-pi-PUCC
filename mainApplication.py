from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Conexão com o banco de dados
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='bancodedadoshope'
    )

# Rota para login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    senha = data.get('senha')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM login JOIN pacientes ON login.userID = pacientes.pacienteID WHERE email=%s AND senha=%s", (email, senha))
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
