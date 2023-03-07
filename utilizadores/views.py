from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Pessoa
from django.shortcuts import redirect
from .forms import *
#from .tables import UtilizadoresTable
#from .filters import UtilizadoresFilter
from django.contrib import messages
from django.contrib.auth import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import F
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView





def login_action(request):
    ''' Fazer login na plataforma do dia aberto e gestão de acessos à plataforma '''
    if request.user.is_authenticated: 
        return redirect("utilizadores:logout")   
    else:
        u=""
    msg=False
    error=""
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username=="" or password=="":
                msg=True
                error="Todos os campos são obrigatórios!"
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                utilizador = Pessoa.objects.get(id=user.id)
                if utilizador.valido=="False": 
                    msg=True
                    error="O seu registo ainda não foi validado"
                elif utilizador.valido=="Rejeitado":
                    msg=True
                    error="O seu registo não é válido"
                else:
                    login(request, user)
                    return redirect('utilizadores:mensagem',1)
            else:
                msg=True
                error="O nome de utilizador ou a palavra-passe inválidos!"
    form = LoginForm()
    return render(request=request,
                  template_name="utilizadores/login.html",
                  context={"form": form,"msg": msg, "error": error, 'u': u})






def logout_action(request):
    ''' Fazer logout na plataforma '''
    logout(request)
    return redirect('utilizadores:mensagem',2)





def alterar_password(request):
    ''' Alterar a password do utilizador '''
    if request.user.is_authenticated:    
        user = get_user(request)
        if user.groups.filter(name = "Coordenador").exists():
            u = "Coordenador"
        elif user.groups.filter(name = "Administrador").exists():
            u = "Administrador"
        elif user.groups.filter(name = "ProfessorUniversitario").exists():
            u = "ProfessorUniversitario"
        elif user.groups.filter(name = "Colaborador").exists():
            u = "Colaborador"
        elif user.groups.filter(name = "Participante").exists():
            u = "Participante" 
        else:
            u=""     
    else:
        return redirect('utilizadores:mensagem',5)
    msg=False
    error="" 
    if request.method == 'POST':
        form = AlterarPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('utilizadores:mensagem',6)
        else:
            msg=True
            error="Passwords Incorretas!"
    form = AlterarPasswordForm(user=request.user)
    return render(request=request,
                  template_name="utilizadores/alterar_password.html",
                  context={"form": form,"msg": msg, "error": error, 'u': u})    

def enviar_email_validar(request,nome,id):
    ''' Envio de email quando o utilizador é validado na pagina consultar utilizadores '''  
    msg="A enviar email a "+nome+" a informar que o seu registo foi validado"
    user_check_var = user_check(request=request, user_profile=[Coordenador, Administrador])
    if user_check_var.get('exists') == False: 
        return user_check_var.get('render')
    request.session['consultar_utilizadores'] = request.META.get('HTTP_REFERER', '/')
    return render(request=request,
                  template_name="utilizadores/enviar_email_validar.html",
                  context={"msg": msg, "id":id})



def enviar_email_rejeitar(request,nome,id):  
    ''' Envio de email quando o utilizador é rejeitado na pagina consultar utilizadores '''
    msg="A enviar email a "+nome+" a informar que o seu registo foi rejeitado"
    user_check_var = user_check(request=request, user_profile=[Coordenador, Administrador])
    if user_check_var.get('exists') == False: 
        return user_check_var.get('render')
    request.session['consultar_utilizadores'] = request.META.get('HTTP_REFERER', '/')
    return render(request=request,
                  template_name="utilizadores/enviar_email_rejeitar.html",
                  context={"msg": msg, "id":id})





def home(request):
    ''' Pagina principal da plataforma '''
    if request.user.is_authenticated:    
        user = get_user(request)
        if user.groups.filter(name = "Coordenador").exists():
            u = "Coordenador"
        elif user.groups.filter(name = "Administrador").exists():
            u = "Administrador"
        elif user.groups.filter(name = "ProfessorUniversitario").exists():
            u = "ProfessorUniversitario"
        elif user.groups.filter(name = "Colaborador").exists():
            u = "Colaborador"
        elif user.groups.filter(name = "Participante").exists():
            u = "Participante" 
        else:
            u=""     
    else:
        u=""
    
    return render(request, "inicio.html",context={ 'u': u})

def mensagem(request, id, *args, **kwargs):
    ''' Template de mensagens informativas/erro/sucesso '''

    if request.user.is_authenticated:    
        user = get_user(request)
        if user.groups.filter(name = "Coordenador").exists():
            u = "Coordenador"
        elif user.groups.filter(name = "Administrador").exists():
            u = "Administrador"
        elif user.groups.filter(name = "ProfessorUniversitario").exists():
            u = "ProfessorUniversitario"
        elif user.groups.filter(name = "Colaborador").exists():
            u = "Colaborador"
        elif user.groups.filter(name = "Participante").exists():
            u = "Participante" 
        else:
            u=""     
    else:
        u = ""


    if id == 400 or id == 500:
        user = get_user(request)
        m = "Erro no servidor"
        tipo = "error"
    elif id == 1:
        user = get_user(request)
        m = "Bem vindo(a) "+user.first_name
        tipo = "info"

    elif id == 2:
        m = "Até á próxima!"
        tipo = "info"

    elif id == 3:
        m = "Registo feito com sucesso!"
        tipo = "sucess"

    elif id == 4:
        m = "É necessário fazer login primeiro"
        tipo = "error"

    elif id == 5:
        m = "Não permitido"
        tipo = "error"
    elif id == 6:
        m = "Senha alterada com sucesso!"
        tipo = "success"    
    elif id == 7:
        m = "Conta apagada com sucesso"
        tipo = "success"   
    elif id == 8:
        m = "Perfil alterado com sucesso"
        tipo = "success" 
    elif id == 9:
        m = "Perfil criado com sucesso"
        tipo = "success" 
    elif id == 10:
        m = "Não existem notificações"
        tipo = "info"
    elif id == 11:
        m = "Esta tarefa deixou de estar atribuída"
        tipo = "error"
    elif id == 12:
        m = "Ainda não é permitido criar inscrições"
        tipo = "error"
    elif id == 13:
        m = "Erro ao apagar dados do utilizador"
        tipo = "error" 
    elif id == 14:
        m = "Não existem mensagens"
        tipo = "info"  
    elif id == 15:
        m = "Este colaborador tem tarefas iniciadas pelo que apenas deverá ser apagado quando estas estiverem concluidas"
        tipo = "info"  
    elif id == 16:
        m = "Para puder apagar a sua conta deverá concluir primeiro as tarefas que estão iniciadas"
        tipo = "info"                 
    elif id == 17:
        m = "A sua disponibilidade foi alterada com sucesso"
        tipo = "success"
    elif id == 18:
        m = "Antes de poder ver dados e estatísticas é preciso configurar um Dia Aberto."
        tipo = "error"
    else:
        m = "Esta pagina não existe"
        tipo = "error"                                     

    
    continuar = "on" 
    if id == 400 or id == 500:
        continuar = "off" 
    return render(request=request,
        template_name="mensagem.html", context={'m': m, 'tipo': tipo ,'u': u, 'continuar': continuar,})


