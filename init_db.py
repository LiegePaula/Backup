import sqlite3

conn = sqlite3.connect('db/database.db')
cursor = conn.cursor()

# Tabela de escolas
cursor.execute("""
CREATE TABLE IF NOT EXISTS Escolas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    email TEXT,
    endereco TEXT,
    cidade TEXT,
    estado TEXT,
    cep TEXT,
    tipo_escola TEXT CHECK(tipo_escola IN ('Pública', 'Privada')) NOT NULL,
    status TEXT CHECK(status IN ('Ativa', 'Inativa')) DEFAULT 'Ativa',
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

# Tabela de alunos
cursor.execute("""
CREATE TABLE IF NOT EXISTS Alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    email TEXT,
    data_nascimento DATE,
    id_escola INTEGER,
    endereco TEXT,
    cidade TEXT,
    estado TEXT,
    cep TEXT,
    status TEXT CHECK(status IN ('Ativo', 'Inativo', 'Graduado', 'Transferido')) DEFAULT 'Ativo',
    data_matricula TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_ultima_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_escola) REFERENCES Escolas(id)
);
""")

conn.commit()
conn.close()
