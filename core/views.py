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
                return redirect('novo_agendamento_paciente')
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
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='core_consulta';")
    return redirect('lista_clientes')

def gerar_calendario():
    import calendar
    from datetime import datetime, timedelta
    hoje = datetime.now().date()
    cal = calendar.Calendar(firstweekday=6) # 6 = Domingo
    semanas = cal.monthdatescalendar(hoje.year, hoje.month)
    
    calendario_dados = []
    for semana in semanas:
        dias_semana = []
        for dia in semana:
            disponivel = False
            # Disponível se for no futuro, no mesmo mês, e dia de semana (seg a sex)
            if dia > hoje and dia.month == hoje.month and dia.weekday() < 5:
                disponivel = True
            
            dias_semana.append({
                'iso': dia.strftime('%Y-%m-%d'),
                'dia': dia.day,
                'disponivel': disponivel,
            })
        calendario_dados.append(dias_semana)
        
        meses = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    return {
        'mes_nome': meses[hoje.month],
        'ano': hoje.year,
        'semanas': calendario_dados
    }

def get_agendamentos_bloqueados(exclude_id=None):
    import json
    consultas = Consulta.objects.all()
    if exclude_id:
        consultas = consultas.exclude(id_consulta=exclude_id)
        
    bloqueados = {}
    for c in consultas:
        if c.data and c.hora:
            data_str = c.data if isinstance(c.data, str) else c.data.strftime('%Y-%m-%d')
            hora_str = c.hora[:5] if isinstance(c.hora, str) else c.hora.strftime('%H:%M')
            if data_str not in bloqueados:
                bloqueados[data_str] = []
            bloqueados[data_str].append(hora_str)
    return json.dumps(bloqueados)

# 6. Agendar Consulta (Recepção)
def agendar_consulta_view(request):
    sucesso = False
    usuarios = Usuario.objects.all().order_by('nome')
    calendario = gerar_calendario()
    bloqueados_json = get_agendamentos_bloqueados()
    
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
                
    return render(request, 'core/agendar_consulta.html', {'usuarios': usuarios, 'sucesso': sucesso, 'calendario': calendario, 'bloqueados_json': bloqueados_json})

# 7. Consultar Agendamentos (Painel do Paciente)
def consultar_agendamentos_view(request):
    paciente_id = request.session.get('paciente_id')
    
    if not paciente_id:
        return redirect('home')
        
    paciente = get_object_or_404(Usuario, id_usuario=paciente_id)
    consultas = Consulta.objects.filter(paciente=paciente).order_by('data', 'hora')
        
    return render(request, 'core/consultar_agendamentos.html', {'consultas': consultas, 'paciente': paciente})

# 8. Agendar Nova Consulta (Pelo próprio Paciente)
def novo_agendamento_paciente_view(request):
    paciente_id = request.session.get('paciente_id')
    
    if not paciente_id:
        return redirect('home')
        
    paciente = get_object_or_404(Usuario, id_usuario=paciente_id)
    sucesso = False
    calendario = gerar_calendario()
    bloqueados_json = get_agendamentos_bloqueados()
    
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        data_str = request.POST.get('data')
        hora_str = request.POST.get('hora')
        
        if tipo and data_str and hora_str:
            try:
                Consulta.objects.create(
                    paciente=paciente,
                    tipo=tipo,
                    data=data_str,
                    hora=hora_str
                )
                sucesso = True
                return redirect('consultar_agendamentos')
            except Exception as e:
                print("ERRO AO SALVAR CONSULTA DO PACIENTE:", e)
                
    return render(request, 'core/agendamento_paciente.html', {'paciente': paciente, 'calendario': calendario, 'bloqueados_json': bloqueados_json})

# 9. Editar Agendamento (Paciente)
def editar_agendamento_paciente_view(request, id_consulta):
    paciente_id = request.session.get('paciente_id')
    if not paciente_id:
        return redirect('home')
        
    consulta = get_object_or_404(Consulta, id_consulta=id_consulta, paciente__id_usuario=paciente_id)
    calendario = gerar_calendario()
    bloqueados_json = get_agendamentos_bloqueados(exclude_id=id_consulta)
    
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        data_str = request.POST.get('data')
        hora_str = request.POST.get('hora')
        
        if tipo and data_str and hora_str:
            consulta.tipo = tipo
            consulta.data = data_str
            consulta.hora = hora_str
            consulta.save()
            return redirect('consultar_agendamentos')
            
    return render(request, 'core/editar_agendamento_paciente.html', {'consulta': consulta, 'calendario': calendario, 'bloqueados_json': bloqueados_json})

# 10. Apagar Agendamento (Paciente)
def apagar_agendamento_paciente_view(request, id_consulta):
    paciente_id = request.session.get('paciente_id')
    if not paciente_id:
        return redirect('home')
        
    consulta = get_object_or_404(Consulta, id_consulta=id_consulta, paciente__id_usuario=paciente_id)
    consulta.delete()
    return redirect('consultar_agendamentos')

# 11. Editar Perfil (Paciente)
def editar_perfil_paciente_view(request):
    paciente_id = request.session.get('paciente_id')
    if not paciente_id:
        return redirect('home')
        
    paciente = get_object_or_404(Usuario, id_usuario=paciente_id)
    erro = None
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        if len(senha) < 8:
            erro = "A senha deve ter no mínimo 8 caracteres."
        elif Usuario.objects.filter(email=email).exclude(id_usuario=paciente_id).exists():
            erro = "Este e-mail já está cadastrado por outra pessoa."
        else:
            paciente.nome = nome
            paciente.telefone = telefone
            paciente.email = email
            paciente.senha = senha
            paciente.save()
            return redirect('consultar_agendamentos')
            
    return render(request, 'core/editar_perfil.html', {'paciente': paciente, 'erro': erro})