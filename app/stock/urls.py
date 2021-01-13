from django.urls import include, path
from rest_framework import routers
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.listProdutos, name="Produtos"),
    path('add', views.addProduto, name='Criar Produto'),
    path('update/<str:pk>/', views.updateProduto, name='Editar Produto'),
    path('delete/<str:pk>/', views.deleteProduto, name='Excluir Produto'),
]