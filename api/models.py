from datetime import date
from django.db import models

# Create your models here.
class Livro (models.Model):
    nome = models.CharField(max_length=100)
    data_de_publicacao = date.today()
    def __str__(self):
        return self.nome