from rest_framework import serializers

from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id','codigo_produto','nome_produto','valor_produto']