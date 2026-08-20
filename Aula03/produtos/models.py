from django.db import models

class Categoria (models.Model):
    nome = models.CharField(max_length=100)

# Create your models here.
class Produto (models.Model):
    nome = models.CharField(max_length=120)
    quantidade = models.PositiveIntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    # Aqui atraves da chave relacionamos a categoria e o produto
    categoria = models.ForeignKey(
        Categoria,
        # Serve para caso exclua a categoria nao exclua o produto
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = "produtos"
    )
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.nome} (qtde={self.quantidade})"

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(
        unique = True
    )

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    STATUS_CHOICES = [
        ("PENDENTE", "Pendente"),
        ("PAGO", "Pago"),
        ("ENVIADO", "Enviado"),
        ("ENTREGUE", "Entregue"),
        ("CANCELADO", "Cancelado")
    ]

    # Relacionando cliente com pedidos

    cliente = models.ForeignKey(
        Cliente,
        on_delete = models.CASCADE,
        related_name = "pedidos",
    )

    data_pedido = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices = STATUS_CHOICES,
        default = "PENDETE"
    )

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nome}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete = models.CASCADE,
        related_name = "itens"
    )

    produto = models.ForeignKey(
        Produto,
        on_delete = models.PROTECT
    )

    quantidade = models.PositiveIntegerField()

    preco_unitario = models.DecimalField(
        max_digits = 10,
        decimal_places = 2
    )

    def subtotal(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"