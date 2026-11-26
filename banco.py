import mysql.connector
import pandas as pandas

# Construir a conexão com o servidor MYSQL
def conectar():
    conexao = mysql.connector.connect(
        host= "localhost", # onde está mysql
        user = "app_hortifruti", # o user do app
        password= "App@Horti2026", # a senha do user
        database = "hortifruti" # o banco que vamos usar
    )
    return conexao

def cadastrar(nome, categoria, preco):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO produto (nome, categoria, preco) VALUES (%s, %s, %s)",
        (nome, categoria, preco)
    )
    conexao.commit()
    cursor.close()
    conexao.close()