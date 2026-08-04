from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from datetime import datetime
from .models import Usuario, Consulta

# 1. Página de Boas-Vindas / Login
def home_view(request):
    erro = None
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            paciente = Usuario.objects.get(email=email, senha=senha)
            request.session['paciente_id'] = paciente.id_usuario
            return redirect('consultar_agendamentos')
        except Usuario.DoesNotExist:
            erro = "E-mail ou senha incorretos."
            
    return render(request, 'core/home.html', {'erro': erro})

# 1.5 Auto-cadastro do paciente
def cadastro_paciente_view(request):
    erro = None
    if request.method == 'POST':
        nome = request.POST.get('nome')
        nascimento_str = request.POST.get('nascimento')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if len(senha) < 8:
            erro = "A senha deve ter no mínimo 8 caracteres."
        elif Usuario.objects.filter(email=email).exists():
            erro = "Este e-mail já está cadastrado."
        else:
            try:
                # Calcula idade
                nascimento = datetime.strptime(nascimento_str, '%Y-%m-%d').date()
                hoje = datetime.now().date()
                idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

                paciente = Usuario.objects.create(
                    nome=nome,
                    idade=idade,
                    telefone=telefone,
                    email=email,
                    senha=senha
                )
                request.session['paciente_id'] = paciente.id_usuario
                return redirect('consultar_agendamentos')
            except Exception as e:
                erro = "Ocorreu um erro ao realizar o cadastro."

    return render(request, 'core/cadastro_paciente.html', {'erro': erro})

# Sair (Logout)
def sair_view(request):
    request.session.flush()
    return redirect('home')

# 2. Tela de Cadastro pela Recepção (Mantida)
def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        nascimento_str = request.POST.get('nascimento')
        telefone = request.POST.get('telefone')
        
        # Calcular Idade (simples)
        nascimento = datetime.strptime(nascimento_str, '%Y-%m-%d').date()
        hoje = datetime.now().date()
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        
        # Salvar no BD
        Usuario.objects.create(nome=nome, idade=idade, telefone=telefone)
        return render(request, 'core/hello.html', {'nome': nome, 'idade': idade, 'telefone': telefone})
        
    return render(request, 'core/cadastro.html')

# 3. Lista de Clientes (Painel Admin)
def lista_view(request):
    usuarios = Usuario.objects.all()
    return render(request, 'core/lista_usuarios.html', {'usuarios': usuarios})

# 4. Excluir um usuário (Lixeira)
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

# 6. Agendar Consulta (Recepção)
def agendar_consulta_view(request):
    sucesso = False
    usuarios = Usuario.objects.all().order_by('nome')
    
    if request.method == 'POST':
        id_paciente = request.POST.get('paciente')
        tipo = request.POST.get('tipo')
        data_str = request.POST.get('data')
        hora_str = request.POST.get('hora')
        
        if id_paciente and tipo and data_str and hora_str:
            paciente = get_object_or_404(Usuario, id_usuario=id_paciente)
            try:
                Consulta.objects.create(
                    paciente=paciente,
                    tipo=tipo,
                    data=data_str,
                    hora=hora_str
                )
                sucesso = True
            except Exception as e:
                print("ERRO AO SALVAR CONSULTA:", e)
                
    return render(request, 'core/agendar_consulta.html', {'usuarios': usuarios, 'sucesso': sucesso})

# 7. Consultar Agendamentos (Painel do Paciente)
def consultar_agendamentos_view(request):
    paciente_id = request.session.get('paciente_id')
    
    if not paciente_id:
        return redirect('home')
        
    paciente = get_object_or_404(Usuario, id_usuario=paciente_id)
    consultas = Consulta.objects.filter(paciente=paciente).order_by('data', 'hora')
        
    return render(request, 'core/consultar_agendamentos.html', {'consultas': consultas, 'paciente': paciente})