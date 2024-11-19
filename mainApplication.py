from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from dbConnection import mySql

app = Flask(__name__)

# Rota para renderizar o formulário
@app.route('/')
def index():
    return render_template('../front-end/view/index.html')

# API para obter dados do cliente
@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    cursor = mySql.connection.cursor()
    query = """
    SELECT 
        pacientes.pacienteID, 
        pacientes.nomePaciente, 
        pacientes.dataNascPaciente, 
        pacientes.pacienteCPF, 
        pacientes.fotoPaciente,
        login.email,
        login.senha
    FROM 
        pacientes
    LEFT JOIN 
        login
    ON 
        pacientes.pacienteID = login.userID;
    """
    cursor.execute(query)
    result = cursor.fetchall()

    # Formatando os resultados em JSON
    clientes = [
        {
            "id": row[0],
            "nome": row[1],
            "dataNascimento": row[2],
            "cpf": row[3],
            "foto": row[4],
            "email": row[5],
            "senha": row[6]
        }
        for row in result
    ]
    cursor.close()
    return jsonify(clientes)

if __name__ == '__main__':
    app.run(debug=True)
