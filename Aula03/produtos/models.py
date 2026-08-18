from django.db import models

# Create your models here.
class Produto (models.Model):
    nome = models.CharField(max_length=120)
    quantidade = models.PositiveIntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"{self.nome} (qtde={self.quantidade})"