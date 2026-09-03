from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from .models import (Produto, Categoria, Cliente, Pedido, ItemPedido)
from .serializers import (ProdutoSerializer, CategoriaSerializer, ClienteSerializer, PedidoSerializer, ItemPedidoSerializer, StatusPedidoSerializer)

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá Django ! Aplicacoes Web 2026 - 2 - Aula 03 Loja de Produtos")

# Categoria que permite fazer o crude do Produto
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by("-id")
    serializer_class = ProdutoSerializer

# Categoria
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by("-id")
    serializer_class = CategoriaSerializer

# Cliente
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by("-id")
    serializer_class = ClienteSerializer

# Pedido
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all().order_by("-id")
    serializer_class = PedidoSerializer

# ItemPedido
class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all().order_by("-id")
    serializer_class = ItemPedidoSerializer

class StatusPedidoViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Pedido.objects.all()
    serializer_class = StatusPedidoSerializer