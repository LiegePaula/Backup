from models.escola import criar_escola, listar_escolas
from models.aluno import criar_aluno, listar_alunos

# Criar algumas escolas
criar_escola("Colégio Central", "Pública", telefone="123456789")
criar_escola("Instituto Elite", "Privada")

# Criar alguns alunos
criar_aluno("Lucas Almeida", id_escola=1)
criar_aluno("Maria Fernanda")  # sem escola

# Listar
print("🏫 Escolas:")
for escola in listar_escolas():
    print(escola)

print("\n👨‍🎓 Alunos:")
for aluno in listar_alunos():
    print(aluno)
