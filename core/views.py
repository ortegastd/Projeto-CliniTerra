from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from datetime import datetime
from .models import Usuario, Consulta

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

# 6. Cadastro de Consulta
def cadastro_consulta_view(request):
    sucesso = False
    usuarios = Usuario.objects.all().order_by('nome')

    if request.method == 'POST':
        id_usuario = request.POST.get('usuario')
        tipo = request.POST.get('tipo')
        data_consulta = request.POST.get('data')
        hora_consulta = request.POST.get('hora')
        observacoes = request.POST.get('observacoes')

        if id_usuario and tipo and data_consulta and hora_consulta:
            try:
                usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
                Consulta.objects.create(
                    usuario=usuario,
                    tipo=tipo,
                    data=data_consulta,
                    hora=hora_consulta,
                    observacoes=observacoes,
                )
                sucesso = True
            except Exception as e:
                print("ERRO AO SALVAR CONSULTA:", e)

    return render(request, 'core/cadastro_consulta.html', {
        'usuarios': usuarios,
        'tipos': Consulta.TIPO_CHOICES,
        'cadastrado': sucesso,
    })

# 7. Painel Administrativo de Consultas
def lista_consultas_view(request):
    consultas = Consulta.objects.select_related('usuario').all()
    return render(request, 'core/lista_consultas.html', {'consultas': consultas})

# 8. Excluir consulta individual
def excluir_consulta_view(request, id_consulta):
    consulta = get_object_or_404(Consulta, id_consulta=id_consulta)
    consulta.delete()
    return redirect('lista_consultas')

# 9. Consultar Agendamentos (Paciente busca as próprias consultas)
def consultar_agendamentos_view(request):
    consultas = None
    buscou = False
    nome = request.GET.get('nome', '').strip()
    telefone = request.GET.get('telefone', '').strip()

    if nome or telefone:
        buscou = True
        filtros = {}
        if nome:
            filtros['usuario__nome__icontains'] = nome
        if telefone:
            filtros['usuario__telefone__icontains'] = telefone

        consultas = Consulta.objects.select_related('usuario').filter(**filtros)

    return render(request, 'core/consultar_agendamentos.html', {
        'consultas': consultas,
        'buscou': buscou,
        'nome': nome,
        'telefone': telefone,
    })