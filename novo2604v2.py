import sqlite3
import streamlit as st

# Banco
def iniciar_banco():
    conexao = sqlite3.connect("banco_de_dados.db")
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        );
    ''')
    conexao.commit()
    return conexao, cursor

def cadastrar_usuario(nome, email):
    conexao, cursor = iniciar_banco()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()

def listar_usuarios():
    conexao, cursor = iniciar_banco()
    cursor.execute("SELECT * FROM usuarios")
    return cursor.fetchall()

def buscar_usuario_por_id(id):
    conexao, cursor = iniciar_banco()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    return cursor.fetchone()

def atualizar_usuario(id, nome, email):
    conexao, cursor = iniciar_banco()
    cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (nome, email, id))
    conexao.commit()

def deletar_usuario(id):
    conexao, cursor = iniciar_banco()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conexao.commit()

# Interface
def main():
    st.title("CRUD com Streamlit + SQLite")

    # Expander: Cadastrar
    with st.expander("📥 Cadastrar novo usuário", expanded=True):
        nome = st.text_input("Nome", key="nome_cadastro")
        email = st.text_input("Email", key="email_cadastro")
        if st.button("Cadastrar"):
            if nome and email:
                cadastrar_usuario(nome, email)
                st.success("Usuário cadastrado com sucesso!")
            else:
                st.warning("Preencha nome e email.")

    # Expander: Buscar
    with st.expander("🔍 Buscar usuário por ID", expanded=True):
        id_busca = st.text_input("ID para buscar", key="id_busca")
        if st.button("Buscar"):
            if id_busca:
                usuario = buscar_usuario_por_id(id_busca)
                if usuario:
                    st.info(f"ID: {usuario[0]} | Nome: {usuario[1]} | Email: {usuario[2]}")
                else:
                    st.warning("Usuário não encontrado.")

    # Expander: Atualizar
    with st.expander("✏️ Atualizar usuário", expanded=True):
        id_update = st.text_input("ID para atualizar", key="id_update")
        nome_update = st.text_input("Novo nome", key="nome_update")
        email_update = st.text_input("Novo email", key="email_update")
        if st.button("Atualizar"):
            if id_update and nome_update and email_update:
                atualizar_usuario(id_update, nome_update, email_update)
                st.success("Usuário atualizado!")
            else:
                st.warning("Preencha todos os campos.")

    # Expander: Deletar
    with st.expander("🗑️ Deletar usuário", expanded=True):
        id_delete = st.text_input("ID para deletar", key="id_delete")
        if st.button("Deletar"):
            if id_delete:
                deletar_usuario(id_delete)
                st.success("Usuário deletado!")
            else:
                st.warning("Digite um ID.")

    # Listar usuários (fora dos expanders)
    st.subheader("📄 Lista de usuários")
    if st.button("Atualizar lista"):
        usuarios = listar_usuarios()
        if usuarios:
            for u in usuarios:
                st.write(f"ID: {u[0]} | Nome: {u[1]} | Email: {u[2]}")
        else:
            st.info("Nenhum usuário cadastrado ainda.")

if __name__ == "__main__":
    main()