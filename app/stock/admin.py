from django.contrib import admin
from stock.models import Produto

# Register your models here.
# Define the admin class
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo_produto','nome_produto','valor_produto','created_produto','ativo_produto')
    fields = [('codigo_produto','nome_produto'),'valor_produto','ativo_produto', 'created_produto']
