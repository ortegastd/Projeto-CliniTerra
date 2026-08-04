from django.contrib import admin
from django.urls import path
from core.views import (
    home_view, cadastro_view, lista_view, limpar_banco_view, 
    excluir_usuario_view, agendar_consulta_view, consultar_agendamentos_view,
    cadastro_paciente_view, sair_view, novo_agendamento_paciente_view,
    editar_agendamento_paciente_view, apagar_agendamento_paciente_view,
    editar_perfil_paciente_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),                                            # Login do Paciente
    path('registrar/', cadastro_paciente_view, name='cadastro_paciente'),        # Auto-cadastro do Paciente
    path('sair/', sair_view, name='sair'),                                       # Logout
    path('meu-painel/', consultar_agendamentos_view, name='consultar_agendamentos'), # Dashboard do Paciente
    path('meu-agendamento/', novo_agendamento_paciente_view, name='novo_agendamento_paciente'), # Agendamento do paciente
    path('meu-painel/editar-consulta/<int:id_consulta>/', editar_agendamento_paciente_view, name='editar_agendamento_paciente'),
    path('meu-painel/cancelar-consulta/<int:id_consulta>/', apagar_agendamento_paciente_view, name='apagar_agendamento_paciente'),
    path('meu-painel/editar-perfil/', editar_perfil_paciente_view, name='editar_perfil_paciente'),
    path('cadastro-recepcao/', cadastro_view, name='cadastro'),                  # Cadastro pela Recepção
    path('clientes/', lista_view, name='lista_clientes'),                        # Painel Administrativo
    path('limpar/', limpar_banco_view, name='limpar_banco'),                     # Apagar tudo
    path('excluir/<int:id_usuario>/', excluir_usuario_view, name='excluir_usuario'), # Lixeira
    path('agendar/', agendar_consulta_view, name='agendar_consulta'),            # Agendar pela recepção
]