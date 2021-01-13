from django.db import models
from django.contrib import admin
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Produto(models.Model):
    codigo_produto = models.CharField(max_length=20)
    nome_produto = models.CharField(max_length=100)
    valor_produto = models.DecimalField(max_digits=6, decimal_places=2)
    created_produto = models.DateTimeField(default=timezone.now)
    ativo_produto = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_produto
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('produto-detail', args=[str(self.id)])