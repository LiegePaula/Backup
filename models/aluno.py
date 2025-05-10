import sqlite3

DB_PATH = 'db/database.db'

def criar_aluno(nome, id_escola=None, telefone=None, email=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Alunos (nome, telefone, email, id_escola)
        VALUES (?, ?, ?, ?)
    """, (nome, telefone, email, id_escola))
    conn.commit()
    conn.close()

def listar_alunos():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Alunos.nome, Escolas.nome
        FROM Alunos
        LEFT JOIN Escolas ON Alunos.id_escola = Escolas.id
    """)
    alunos = cursor.fetchall()
    conn.close()
    return alunos
