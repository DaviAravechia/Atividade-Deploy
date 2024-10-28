from django.db import models

# Create your models here.
class Livro (models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    vendas = models.IntegerField()
    def __str__(self):
        return self.nome