from django.contrib import admin
from django.urls import path
from core.views import (
    cadastro_view, lista_view, excluir_usuario_view, limpar_banco_view,
    cadastro_consulta_view, lista_consultas_view, excluir_consulta_view,
    consultar_agendamentos_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cadastro_view, name='cadastro'),
    path('clientes/', lista_view, name='lista_clientes'),
    
    # GARANTA QUE ESSAS DUAS LINHAS ESTÃO AQUI E SALVAS:
    path('clientes/excluir/<int:id_usuario>/', excluir_usuario_view, name='excluir_usuario'),
    path('clientes/limpar-tudo/', limpar_banco_view, name='limpar_banco'),

    path('consultas/nova/', cadastro_consulta_view, name='cadastro_consulta'),
    path('consultas/', lista_consultas_view, name='lista_consultas'),
    path('consultas/excluir/<int:id_consulta>/', excluir_consulta_view, name='excluir_consulta'),
    path('agendamentos/', consultar_agendamentos_view, name='consultar_agendamentos'),
]