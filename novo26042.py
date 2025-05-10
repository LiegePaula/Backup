import sqlite3

# Conecta ao banco de dados
conexao = sqlite3.connect('banco_de_dados.db')
cursor = conexao.cursor()

# Cria a tabela se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
''')
conexao.commit()

# -------- Funções do CRUD -------- #

def cadastrar_usuario():
    nome = input("Digite o nome: ").strip()
    email = input("Digite o email: ").strip()
    try:
        if not nome or not email:
            raise ValueError("Nome e email não podem ser vazios.")
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        conexao.commit()
        print("Usuário cadastrado com sucesso.")
    except sqlite3.IntegrityError:
        print("Email já cadastrado.")
        return menu()
    except ValueError as e:
        print(e)
        return menu()
    

def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    if usuarios:
        print("\n--- Lista de usuários ---")
        for u in usuarios:
            print(f"ID: {u[0]}, Nome: {u[1]}, Email: {u[2]}")
    else:
        print("Nenhum usuário encontrado.")

def buscar_usuario_por_id():
    try:
        id = int(input("Digite o ID do usuário: "))
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
        usuario = cursor.fetchone()
        if usuario:
            print(f"\nUsuário encontrado: ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}")
        else:
            print("Usuário não encontrado.")
    except ValueError:
        print("ID inválido.")

def atualizar_usuario():
    try:
        id = int(input("Digite o ID do usuário a ser atualizado: "))
        nome = input("Novo nome (deixe em branco para não alterar): ").strip()
        email = input("Novo email (deixe em branco para não alterar): ").strip()
        if nome:
            cursor.execute("UPDATE usuarios SET nome = ? WHERE id = ?", (nome, id))
        if email:
            cursor.execute("UPDATE usuarios SET email = ? WHERE id = ?", (email, id))
        conexao.commit()
        print("Usuário atualizado.")
    except ValueError:
        print("ID inválido.")

def deletar_usuario():
    try:
        id = int(input("Digite o ID do usuário a ser deletado: "))
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
        conexao.commit()
        print("Usuário deletado.")
    except ValueError:
        print("ID inválido.")

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