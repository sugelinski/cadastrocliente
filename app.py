from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('clientes.db')
    conn.row_factory = sqlite3.Row
    return conn

# Rota para a página principal (cadastro)
@app.route('/')
def index():
    return render_template('cadastro.html')

# Rota para processar o formulário de cadastro
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    idade = request.form['idade']
    email = request.form['email']

    con = get_db_connection()
    con.execute('INSERT INTO clientes (nome, idade, email) VALUES (?, ?, ?)', (nome, idade, email))
    con.commit()
    con.close()
    
    return redirect('/')

# Rota para inicializar o banco de dados
@app.cli.command('initdb')
def initdb_command():
    con = get_db_connection()
    con.execute('CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER, email TEXT)')
    con.commit()
    con.close()
    print('Banco de dados inicializado.')

if __name__ == '__main__':
    app.run(debug=True)
