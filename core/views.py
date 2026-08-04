from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from datetime import datetime
from .models import Usuario

# 1. Página de Boas-Vindas
def home_view(request):
    return render(request, 'core/home.html')

# 2. Página de Cadastro (Isolada)
def cadastro_view(request):
    sucesso = False  
    
    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        data_nascimento_str = request.POST.get('data_nascimento')
        telefone_informado = request.POST.get('telefone')

        if nome_completo and data_nascimento_str:
            try:
                data_nasc = datetime.strptime(data_nascimento_str, '%Y-%m-%d')
                hoje = datetime.today()
                idade_calculada = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
                
                Usuario.objects.create(nome=nome_completo, id_usuario=None, idade=idade_calculada, telefone=telefone_informado)
                sucesso = True  
            except Exception as e:
                print("ERRO AO SALVAR:", e)

    return render(request, 'core/hello.html', {'cadastrado': sucesso})

# 3. Exibir Banco de Dados Cadastrais
def lista_view(request):
    usuarios = Usuario.objects.all().order_by('-id_usuario')
    return render(request, 'core/lista_usuarios.html', {'usuarios': usuarios})

# 4. Lixeira Individual (❌)
def excluir_usuario_view(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    usuario.delete()
    return redirect('lista_clientes')

# 5. Apagar todos os registros (Botão Vermelho)
def limpar_banco_view(request):
    Usuario.objects.all().delete()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='core_usuario';")
    return redirect('lista_clientes')