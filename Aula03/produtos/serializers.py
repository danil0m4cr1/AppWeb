 # Arquivo serializers responsável por transformar a requisição de informação para salvar no banco de dados no formato de tabela
 # importand da biblioteca rest framework o serializers
from rest_framework import serializers
from .models import (Produto, Categoria, Cliente, ItemPedido, Pedido)

# Criando serializar para Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

# Criando a classe Serializers produtos
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        # fields = ["id","nome","quantidade","preco","created_at"]
        fields = "__all__"

# Cliente
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

# ItemPedido
class ItemPedidoSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField(
        read_only = True
    )

    class Meta:
        model = ItemPedido
        fields = [
            "id",
            "pedido",
            "produto",
            "quantidade",
            "preco_unitario",
            "subtotal"
        ]

    def get_subtotal(self,obj):
        return obj.subtotal()

# Pedido
class PedidoSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField(
        read_only = True
    )

    class Meta:
        model = Pedido
        fields = [
            "id",
            "cliente",
            "data_pedido",
            "statuts",
            "total"
        ]

    def get_total(obj,self):
        return obj.total()


# ItemPedidoDetalhe
class ItemPedidoDetalheSerializer(serializers.ModelSerializer):
    produto_nome = serializers.CharField(
        source = "produto.nome",
        read_only = True
    )

    subtotal = serializers.SerializerMethodField(
        read_only = True
    )

    class Meta:
        model = ItemPedido

        fields = [
            "id",
            "produto",
            "produto_nome",
            "quantidade",
            "preco_unitario",
            "subtotal"
        ]

    def get_subtotal(self, obj):
        return obj.subtotal()

class StatusPedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoDetalheSerializer(
        many = True,
        read_only = True
    )

    total = serializers.SerializerMethodField(
        read_only = True
    )

    class Meta:
        model = Pedido
        
        fields = [
            "id",
            "cliente",
            "descricao",
            "data_pedido",
            "status",
            "itens",
            "total"
        ]

        read_only_fields = [
            "id",
            "cliente",
            "descricao",
            "data_pedido",
            "itens",
            "total"
        ]

    def get_total(self, obj):
        return obj.total()