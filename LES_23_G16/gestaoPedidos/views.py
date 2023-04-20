import smtplib
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from .tables import PedidosTable
from .filters import PedidosFilter
#from django.core.paginator import Paginator
from .models import Pedido,PedidoHorario,Docente,Estado, Outros, Uc
from .forms import PedidoForm,PedidoHorarioForm, UcForm, PedidoOutroForm
from django.shortcuts import HttpResponse,get_object_or_404
import datetime
from django.views.decorators.http import require_POST
from django.core.mail import send_mail, EmailMessage
from django.urls import reverse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Create your views here.

numero_items_por_pagina=10

class consultar_pedidos(SingleTableMixin, FilterView):
    ''' Consultar todos os pedidos com as funcionalidades dos filtros '''
    table_class = PedidosTable
    template_name = 'gestaoPedidos/consultar_pedidos.html'
    filterset_class = PedidosFilter
    table_pagination = {
        'per_page': numero_items_por_pagina
    }


def criar_pedido_horario(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        pform = PedidoForm(request.POST, instance=Pedido())
        phform = PedidoHorarioForm(request.POST, instance=PedidoHorario())
        # check whether it's valid:
        if pform.is_valid() and phform.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            novo_pedido = pform.save(commit=False)
            novo_pedido.datecreation = datetime.datetime.now()
            novo_pedido.estadoid = Estado.objects.get(id=1) #Forçar o estado a criado independentemente do que vem
            novo_pedido.docentepessoaid = Docente.objects.get(pessoaid=request.user.id)
            novo_pedido_horario = phform.save(commit=False)
            novo_pedido_horario.pedidoid = novo_pedido
            novo_pedido.save()
            novo_pedido_horario.save()
            messages.success(request, 'Pedido de Horário criado com sucesso')
            return redirect('gestaoPedidos:consultar_pedidos')
        else:
            for error in pform.errors:
                messages.error(request, pform.errors[error])
            #return HttpResponse(str("Objecto NÃO Criado\npform.is_valid():"+" {}").format(pform.is_valid()))
            return render(request=request,
                template_name="gestaoPedidos/criar_pedido_horario.html", context = {'pedidoform': pform,'horarioForm':phform})
    else:
        # if a GET (or any other method) we'll create a blank form
        pform = PedidoForm(instance=Pedido())
        phform = PedidoHorarioForm(instance=PedidoHorario())
        #cforms = [ChoiceForm(prefix=str(x), instance=Choice()) for x in range(0,3)]
    return render(request=request,
                template_name="gestaoPedidos/criar_pedido_horario.html", context = {'pedidoform': pform,'horarioForm':phform})

def alterar_pedido_horario(request):
        # if this is a POST request we need to process the form data
    idpedido=request.GET.get('id')
    pedido=Pedido.objects.get(id=idpedido)
    pedidohorario=PedidoHorario.objects.get(pedidoid=idpedido)
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        pform = PedidoForm(request.POST, instance=pedido)
        phform = PedidoHorarioForm(request.POST, instance=pedidohorario)
        # check whether it's valid:
        if pform.is_valid() and phform.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            novo_pedido = pform.save(commit=False)
            #novo_pedido.datecreation = datetime.datetime.now()
            novo_pedido.estadoid = Estado.objects.get(id=1) #Forçar o estado a criado independentemente do que vem
            #novo_pedido.docentepessoaid = Docente.objects.get(pessoaid=request.user.id)
            novo_pedido_horario = phform.save()
            #novo_pedido_horario.pedidoid = novo_pedido
            novo_pedido.save()
            novo_pedido_horario.save()
            messages.success(request, 'Pedido de Horário alterado com sucesso')
            return redirect('gestaoPedidos:consultar_pedidos')
        else:
            for error in pform.errors:
                messages.error(request, pform.errors[error])
            #return HttpResponse(str("Objecto NÃO Criado\npform.is_valid():"+" {}").format(pform.is_valid()))
            return render(request=request,
                template_name="gestaoPedidos/criar_pedido_horario.html", context = {'pedidoform': pform,'horarioForm':phform})
    else:
         # if a GET (or any other method) we'll create a form form existing objects

        pform = PedidoForm(instance=pedido)
        phform = PedidoHorarioForm(instance=pedidohorario)
        return render(request=request,
                    template_name="gestaoPedidos/criar_pedido_horario.html", context = {'pedidoform': pform,'horarioForm':phform})

@require_POST
def apagar_pedido_horario(request):
    idpedido=request.POST.get('id')
    pedido=Pedido.objects.get(id=idpedido)
    pedidohorario=PedidoHorario.objects.get(pedidoid=idpedido)
    pedidohorario.delete()
    pedido.delete()
    messages.success(request, 'Pedido de Horário apagado com sucesso')
    return HttpResponseRedirect(request.META['HTTP_REFERER'],)

def criar_pedido_outro(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        pform = PedidoForm(request.POST, instance=Pedido())
        phform = PedidoOutroForm(request.POST, instance=Outros())
        # check whether it's valid:
        if pform.is_valid() and phform.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            novo_pedido = pform.save(commit=False)
            novo_pedido.datecreation = datetime.datetime.now()
            novo_pedido.estadoid = Estado.objects.get(id=1) #Forçar o estado a criado independentemente do que vem
            novo_pedido.docentepessoaid = Docente.objects.get(pessoaid=request.user.id)
            novo_pedido_outro = phform.save(commit=False)
            novo_pedido_outro.pedidoid = novo_pedido
            novo_pedido.save()
            novo_pedido_outro.save()
            messages.success(request, 'Pedido Outro criado com sucesso')
            return redirect('gestaoPedidos:consultar_pedidos')
        else:
            for error in pform.errors:
                messages.error(request, pform.errors[error])
            #return HttpResponse(str("Objecto NÃO Criado\npform.is_valid():"+" {}").format(pform.is_valid()))
            return render(request=request,
                template_name="gestaoPedidos/criar_pedido_outro.html", context = {'pedidoform': pform,'outroForm':phform})
    else:
        # if a GET (or any other method) we'll create a blank form
        pform = PedidoForm(instance=Pedido())
        phform = PedidoOutroForm(instance=Outros())
        #cforms = [ChoiceForm(prefix=str(x), instance=Choice()) for x in range(0,3)]
    return render(request=request,
                template_name="gestaoPedidos/criar_pedido_outro.html", context = {'pedidoform': pform,'outroForm':phform})

def alterar_pedido_outros(request):
        # if this is a POST request we need to process the form data
    idpedido=request.GET.get('id')
    pedido=Pedido.objects.get(id=idpedido)
    pedidooutro=Outros.objects.get(pedidoid=idpedido)
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        pform = PedidoForm(request.POST, instance=pedido)
        phform = PedidoOutroForm(request.POST, instance=pedidooutro)
        # check whether it's valid:
        if pform.is_valid() and phform.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            
            novo_pedido = pform.save(commit=False)
            #novo_pedido.datecreation = datetime.datetime.now()
            novo_pedido.estadoid = Estado.objects.get(id=1) #Forçar o estado a criado independentemente do que vem
            #novo_pedido.docentepessoaid = Docente.objects.get(pessoaid=request.user.id)
            novo_pedido_outro = phform.save()
            #novo_pedido_horario.pedidoid = novo_pedido
            novo_pedido.save()
            novo_pedido_outro.save()
            messages.success(request, 'Pedido Outro alterado com sucesso')
            return redirect('gestaoPedidos:consultar_pedidos')
        else:
            for error in pform.errors:
                messages.error(request, pform.errors[error])
            #return HttpResponse(str("Objecto NÃO Criado\npform.is_valid():"+" {}").format(pform.is_valid()))
            return render(request=request,
                template_name="gestaoPedidos/criar_pedido_outro.html", context = {'pedidoform': pform,'outroForm':phform})
    else:
         # if a GET (or any other method) we'll create a form form existing objects

        pform = PedidoForm(instance=pedido)
        phform = PedidoOutroForm(instance=pedidooutro)
        return render(request=request,
                    template_name="gestaoPedidos/criar_pedido_outro.html", context = {'pedidoform': pform,'outroForm':phform})

@require_POST
def apagar_pedido_outro(request):
    idpedido=request.POST.get('id')
    pedido=Pedido.objects.get(id=idpedido)
    pedidooutro=Outros.objects.get(pedidoid=idpedido)
    pedidooutro.delete()
    pedido.delete()
    messages.success(request, 'Pedido Outro apagado com sucesso')
    return HttpResponseRedirect(request.META['HTTP_REFERER'],)

def criar_pedido_uc(request):
    if request.method == "POST":
        pform = PedidoForm(request.POST, instance=Pedido())
        ucform = UcForm(request.POST, instance=Uc())

        if pform.is_valid() and ucform.is_valid():
            novo_pedido = pform.save(commit=False)
            novo_pedido.datecreation = datetime.datetime.now()
            novo_pedido.estadoid = Estado.objects.get(id=1)
            novo_pedido.docentepessoaid = Docente.objects.get(pessoaid=request.user.id)

            nova_uc = ucform.save(commit=False)
            nova_uc.pedido_ucpedidoid = novo_pedido

            novo_pedido.save()
            nova_uc.save()

            messages.success(request, 'Pedido de UC criado com sucesso')
            return redirect('gestaoPedidos:consultar_pedidos')
        else:
            for error in pform.errors:
                messages.error(request, pform.errors[error])
            return render(request, "gestaoPedidos/criar_pedido_uc.html", context={'pedidoform': pform, 'ucForm': ucform})
    else:
        pform = PedidoForm(instance=Pedido())
        ucform = UcForm(instance=Uc())
        return render(request, "gestaoPedidos/criar_pedido_uc.html", context={'pedidoform': pform, 'ucForm': ucform})

def alterar_pedido_uc(request):
    idpedido = request.GET.get('id')
    pedido = PedidoForm.objects.get(id=idpedido)
    uc = UcForm.objects.get(pedido_ucpedidoid=idpedido)

    if request.method == "POST":
        pform = PedidoForm(request.POST, instance=pedido)
        ucform = UcForm(request.POST, instance=uc)

        if pform.is_valid() and ucform.is_valid():
            novo_pedido = pform.save(commit=False)
            novo_pedido.estadoid = Estado.objects.get(id=1)

            nova_uc = ucform.save()

            novo_pedido.save()
            nova_uc.save()

            messages.success(request, 'Pedido de UC alterado com sucesso')
            return redirect('gestaoPedidos:consultar_pedidos')
        else:
            for error in pform.errors:
                messages.error(request, pform.errors[error])
            return render(request, "gestaoPedidos/criar_pedido_uc.html", context={'pedidoform': pform, 'ucForm': ucform})
    else:
        pform = PedidoForm(instance=pedido)
        ucform = UcForm(instance=uc)
        return render(request, "gestaoPedidos/criar_pedido_uc.html", context={'pedidoform': pform, 'ucForm': ucform})

@require_POST
def apagar_pedido_uc(request):
        idpedido=request.POST.get('id')
        pedido=Pedido.objects.get(id=idpedido)
        pedidouc=pedidouc.objects.get(pedidoid=idpedido)
        pedidouc.delete()
        pedido.delete()
        messages.success(request, 'Pedido de UC apagado com sucesso')
        return HttpResponseRedirect(request.META['HTTP_REFERER'],)

def enviar_email(destinatario, assunto, mensagem, remetente, senha):
    # configurar o email
    email = MIMEMultipart()
    email['From'] = remetente
    email['To'] = destinatario
    email['Subject'] = assunto
    corpo = mensagem
    email.attach(MIMEText(corpo, 'plain'))

    # enviar o email
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()
 # usar o servidor SMTP do Mailtrap
    server.login(remetente, senha)
    texto_email = email.as_string()
    server.sendmail(remetente, destinatario, texto_email)
    server.quit()

def validar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if(pedido.estadoid != 2):
        pedido.estadoid = Estado.objects.get(id=2)
        pedido.save()
    else:
        return redirect('gestaoPedidos:consultar_pedidos')

    # Enviar email de confirmação
    destinatario = 'a68033@ualg.pt'
    assunto = 'Pedido Validado'
    mensagem = f'O pedido {pedido_id} foi validado com sucesso.'
    remetente = 'diogo.raposo@live.com.pt'
    senha = '#####'
    enviar_email(destinatario, assunto, mensagem, remetente, senha)

    messages.success(request, 'Pedido validado com sucesso')
    return redirect('gestaoPedidos:consultar_pedidos')

def nao_validar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if(pedido.estadoid != 3):
        pedido.estadoid = Estado.objects.get(id=3)
        pedido.save()
    else:
         return redirect('gestaoPedidos:consultar_pedidos')

    # Enviar email de confirmação
    destinatario = 'a68033@ualg.pt'
    assunto = 'Pedido Não Validado'
    mensagem = f'O pedido {pedido_id} foi não validado com sucesso.'
    remetente = 'diogo.raposo@live.com.pt'
    senha = '#####'
    enviar_email(destinatario, assunto, mensagem, remetente, senha)

    messages.success(request, 'Pedido não validado com sucesso')
    return redirect('gestaoPedidos:consultar_pedidos')

   #def dispatch(self, request, *args, **kwargs):
 #       user_check_var = user_check(
 #           request=request, user_profile=[Coordenador, Administrador])
 #       if not user_check_var.get('exists'):
  #          return user_check_var.get('render')
    #    return super().dispatch(request, *args, **kwargs)

    #def get_context_data(self, **kwargs):
    #    context = super(SingleTableMixin, self).get_context_data(**kwargs)
    #    table = self.get_table(**self.get_table_kwargs())
    #    table.request = self.request
    #    table.fixed = True
    #    context[self.get_context_table_name(table)] = table
    #    return context
    
    #def get(self, request, *args, **kwargs):
    #     data = Pedido.objects.all()
    #     context = self.get_context_data(**kwargs)
    #     context['table'] = data
    #     return self.render_to_response(context)
