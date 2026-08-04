from django.contrib import admin
from django.urls import path
from core.views import home_view, cadastro_view, lista_view, limpar_banco_view, excluir_usuario_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),                                             # Tela de Boas-Vindas
    path('cadastro/', cadastro_view, name='cadastro'),                           # Tela de Cadastro
    path('clientes/', lista_view, name='lista_clientes'),                        # Banco de Dados Cadastrais
    path('limpar/', limpar_banco_view, name='limpar_banco'),                     # Apagar tudo
    path('excluir/<int:id_usuario>/', excluir_usuario_view, name='excluir_usuario'), # Lixeira individual
]