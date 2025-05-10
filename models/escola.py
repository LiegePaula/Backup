import sqlite3

DB_PATH = 'db/database.db'

def criar_escola(nome, tipo_escola, telefone=None, email=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Escolas (nome, telefone, email, tipo_escola)
        VALUES (?, ?, ?, ?)
    """, (nome, telefone, email, tipo_escola))
    conn.commit()
    conn.close()

def listar_escolas():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Escolas")
    escolas = cursor.fetchall()
    conn.close()
    return escolas
