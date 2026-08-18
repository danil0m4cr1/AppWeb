from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.Model):
    class Meta:
        model = Produto
        fields = ["id", "nome", "quantidade", "precos", "created_at"]