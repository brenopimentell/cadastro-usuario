import sqlite3 

def conectarBD():
    conexao = sqlite3.connect("Clientes.db")
    return conexao

def inserirDados(nome, telefone, endereco):
    conexao = conectarBD()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Clientes(nome, telefone, endereco) VALUES(?, ?, ?)",(nome, telefone, endereco))
    conexao.commit()
    conexao.close()

def listarDados():
    conexao = conectarBD()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Clientes")
    dados = cursor.fetchall()
    cursor.close()
    return dados

    

