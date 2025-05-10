import sqlite3

# Conecta ao banco de dados
conexao = sqlite3.connect('banco_de_dados.db')

# Cria um cursor para executar comandos SQL
cursor = conexao.cursor()

# Cria a tabela usuarios se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nome VARCHAR,
    email VARCHAR
);
''')
def cadastrar_usuario(nome, email):
    # Insere um novo usuário na tabela
    sql = "INSERT INTO usuarios (nome, email) VALUES (?, ?)"
    cursor.execute(sql, (nome, email))
    conexao.commit()

# Cadastra um novo usuário
#cadastrar_usuario('João', 'joaoa@com')


# Commita as alterações
id = 1  # Imagina que isso vem de fora ainda

def listar_usuarios():
    # Seleciona todos os usuários da tabela
    sql = "SELECT * FROM usuarios"
    cursor.execute(sql)
    return cursor.fetchall()

def listar_usuario_por_id(id):
    # Seleciona um usuário específico da tabela
    sql = "SELECT * FROM usuarios WHERE id = ?"
    cursor.execute(sql, (id,))
    return cursor.fetchall()
# Usa uma query segura com parâmetros


# Imprime os resultados
usuarios = listar_usuarios()
for usuario in usuarios:
    print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}")

def atualizar_usuario(id, nome, email):
    # Atualiza os dados de um usuário específico
    sql = "UPDATE usuarios SET nome = ?, email = ? WHERE id = ?"
    cursor.execute(sql, (nome, email, id))
    conexao.commit()

# Atualiza dados na tabela




# Exclui dados da tabela
def excluir_usuario(id):
    # Exclui um usuário específico da tabela
    sql = "DELETE FROM usuarios WHERE id = ?"
    cursor.execute(sql, (id,))
    conexao.commit()

# Exclui um usuário
excluir_usuario(3)
# Imprime os resultados após a exclusão
usuarios = listar_usuarios()

# Fecha a conexão com o banco de dados
conexao.close()

                     # -------- Menu interativo -------- #

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar usuário")
        print("2. Listar todos os usuários")
        print("3. Buscar usuário por ID")
        print("4. Atualizar usuário")
        print("5. Deletar usuário")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            buscar_usuario_por_id()
        elif opcao == "4":
            atualizar_usuario()
        elif opcao == "5":
            deletar_usuario()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

    conexao.close()

# -------- Iniciar programa --------
menu()
                                                                                                                                                                                                                                                       