from django.contrib import admin
from django.urls import path
from core.views import cadastro_view, lista_view, excluir_usuario_view, limpar_banco_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cadastro_view, name='cadastro'),
    path('clientes/', lista_view, name='lista_clientes'),
    
    # GARANTA QUE ESSAS DUAS LINHAS ESTÃO AQUI E SALVAS:
    path('clientes/excluir/<int:id_usuario>/', excluir_usuario_view, name='excluir_usuario'),
    path('clientes/limpar-tudo/', limpar_banco_view, name='limpar_banco'),
]