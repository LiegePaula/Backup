from django.db import models

class Livro(models.Model):
    # Campos do modelo Livro
    titulo = models.CharField(max_length=255)  # Título do livro
    autor = models.CharField(max_length=255)   # Nome(s) do(s) autor(es)
    ano_publicacao = models.IntegerField()     # Ano de publicação
    editora = models.CharField(max_length=255) # Editora do livro
    genero = models.CharField(max_length=100)  # Gênero do livro (romance, ficção, etc.)
    isbn = models.CharField(max_length=20, unique=True, null=True, blank=True) # ISBN do livro
    quantidade = models.IntegerField()         # Quantidade de cópias disponíveis
    descricao = models.TextField()             # Descrição do livro
    status = models.CharField(
        max_length=20, 
        choices=[('disponivel', 'Disponível'), 
                 ('emprestado', 'Emprestado'), 
                 ('reservado', 'Reservado')],
        default='disponivel'
    )  # Status do livro: disponível, emprestado, etc.
    data_cadastro = models.DateTimeField(auto_now_add=True)  # Data de cadastro do livro

    # Representação do objeto Livro
    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano_publicacao})"

    class Meta:
        # Ordenação padrão por título (pode ajustar conforme necessário)
        ordering = ['titulo']
