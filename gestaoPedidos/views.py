import smtplib
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from .tables import PedidosTable
from .filters import PedidosFilter
#from django.core.paginator import Paginator
from .models import Pedido,PedidoHorario,Docente,Estado, Outros, UC, PedidoUC, Funcionario,AnoLetivo
from .forms import PedidoForm,PedidoHorarioForm, PedidoUCForm, PedidoOutroForm, UCForm, EmailForm, ConfirmacaoForm
from django.shortcuts import HttpResponse,get_object_or_404
import datetime
from django.views.decorators.http import require_POST
from django.core.mail import send_mail, EmailMessage, BadHeaderError
from django.urls import reverse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.exceptions import ValidationError
from smtplib import SMTPAuthenticationError
from django.db.models import Q


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
    if request.method == "POST":
        pform = PedidoForm(request.POST, instance=Pedido())
        phform = PedidoOutroForm(request.POST, instance=Outros())
        if pform.is_valid() and phform.is_valid():
            novo_pedido = pform.save(commit=False)
            novo_pedido.datecreation = datetime.datetime.now()
            novo_pedido.estadoid = Estado.objects.get(id=1)
            novo_pedido.docentepessoaid = Docente.objects.get(pessoaid=request.user.id)
            novo_pedido_outro = phform.save(commit=False)
            novo_pedido_outro.pedidoid = novo_pedido
            
            # Validate if there is an existing request with the same subject, description and target date
            if Pedido.objects.filter(assunto=novo_pedido.assunto, descricao=novo_pedido.descricao, dataAlvo=novo_pedido.dataAlvo).exists():
                messages.error(request, 'Já existe um pedido com o mesmo assunto, descrição e data alvo.')
                return redirect('gestaoPedidos:consultar_pedidos')
            
            novo_pedido.save()
            novo_pedido_outro.save()
            messages.success(request, 'Pedido Outro criado com sucesso')
            return redirect('gestaoPedidos:consultar_pedidos')
        else:
            for error in pform.errors:
                messages.error(request, pform.errors[error])
            return render(request=request,
                template_name="gestaoPedidos/criar_pedido_outro.html", context = {'pedidoform': pform,'outroForm':phform})
    else:
        pform = PedidoForm(instance=Pedido())
        phform = PedidoOutroForm(instance=Outros())
    return render(request=request,
                template_name="gestaoPedidos/criar_pedido_outro.html", context = {'pedidoform': pform,'outroForm':phform})


def consultar_pedido_outro(request, id):
    pedido = Pedido.objects.get(id=id)
    pedido_outro = Outros.objects.get(pedidoid=id)

    context = {
        'pedido': pedido,
        'pedido_outro': pedido_outro
    }
    return render(request, 'gestaoPedidos/consultar_pedido_outro.html', context)




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
    idpedido = request.POST.get('id')
    pedido = Pedido.objects.get(id=idpedido)
    pedidooutro = Outros.objects.get(pedidoid=idpedido)

    if(pedido.estadoid.id == 1):
        return redirect('gestaoPedidos:consultar_pedidos')
    
    

    if request.POST.get('confirmar_exclusao') == 'Sim':
        pedidooutro.delete()
        pedido.delete()
        messages.success(request, 'Pedido Outro apagado com sucesso')
        return redirect('gestaoPedidos:consultar_pedidos')
    else:
        return render(request, 'gestaoPedidos/confirmar_exclusão.html', {'pedido': pedido})





def criar_pedido_uc(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        pform = PedidoForm(request.POST, instance=Pedido())
        phform = PedidoUCForm(request.POST, instance=PedidoUC())
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
                template_name="gestaoPedidos/criar_pedido_uc.html", context = {'pedidoform': pform,'UCForm':phform})
    else:
        # if a GET (or any other method) we'll create a blank form
        pform = PedidoForm(instance=Pedido())
        phform = PedidoUCForm(instance=PedidoUC())
        #cforms = [ChoiceForm(prefix=str(x), instance=Choice()) for x in range(0,3)]
    return render(request=request,
                template_name="gestaoPedidos/criar_pedido_uc.html", context = {'pedidoform': pform,'UCForm':phform})

def alterar_pedido_uc(request):
        # if this is a POST request we need to process the form data
    idpedido=request.GET.get('id')
    pedido=Pedido.objects.get(id=idpedido)
    pedidoUC=PedidoUC.objects.get(pedidoid=idpedido)
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        pform = PedidoForm(request.POST, instance=pedido)
        phform = PedidoUCForm(request.POST, instance=pedidoUC)
        # check whether it's valid:
        if pform.is_valid() and phform.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            novo_pedido = pform.save(commit=False)
            #novo_pedido.datecreation = datetime.datetime.now()
            novo_pedido.estadoid = Estado.objects.get(id=1) #Forçar o estado a criado independentemente do que vem
            #novo_pedido.docentepessoaid = Docente.objects.get(pessoaid=request.user.id)
            novo_pedido_UC = phform.save()
            #novo_pedido_horario.pedidoid = novo_pedido
            novo_pedido.save()
            novo_pedido_UC.save()
            messages.success(request, 'Pedido de UC alterado com sucesso')
            return redirect('gestaoPedidos:consultar_pedidos')
        else:
            for error in pform.errors:
                messages.error(request, pform.errors[error])
            #return HttpResponse(str("Objecto NÃO Criado\npform.is_valid():"+" {}").format(pform.is_valid()))
            return render(request=request,
                template_name="gestaoPedidos/criar_pedido_uc.html", context = {'pedidoform': pform,'horarioForm':phform})
    else:
         # if a GET (or any other method) we'll create a form form existing objects

        pform = PedidoForm(instance=pedido)
        phform = PedidoUCForm(instance=pedidoUC)
        return render(request=request,
                    template_name="gestaoPedidos/criar_pedido_uc.html", context = {'pedidoform': pform,'horarioForm':phform})

@require_POST
def apagar_pedido_uc(request):
    idpedido=request.POST.get('id')
    pedido=Pedido.objects.get(id=idpedido)
    pedidoUC=PedidoUC.objects.get(pedidoid=idpedido)
    pedidoUC.delete()
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
    estado = pedido.estadoid
    if pedido.estadoid != 2:
        pedido.estadoid = Estado.objects.get(id=2)
        pedido.save()
    else:
        return redirect('gestaoPedidos:consultar_pedidos')

    if request.method == 'POST':
        form = ConfirmacaoForm(request.POST)
        if form.is_valid():
            mensagem = form.cleaned_data['mensagem']
            if mensagem:
                destinatario = 'a68033@ualg.pt'
                assunto = f'O pedido {pedido_id} encontra-se concluido.'
                mensagem = mensagem or f'O pedido {pedido_id} encontra-se validado.'
                remetente = 'a68033@ualg.pt'
                senha = 'g!2$'
                enviar_email(destinatario, assunto, mensagem, remetente, senha)

                messages.success(request, 'Pedido concluido com sucesso')
                return redirect('gestaoPedidos:consultar_pedidos')
            else:
                messages.warning(request, 'É necessário fornecer uma mensagem para enviar o email.')
                pedido.estadoid = estado  # volta ao estado anterior
                pedido.save()
        else:
            pedido.estadoid = estado  # volta ao estado anterior
            pedido.save()
    else:
        form = ConfirmacaoForm()

    return render(request, 'gestaoPedidos/confirmacao.html', {'form': form})



def nao_validar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    estado = pedido.estadoid
    if pedido.estadoid != 3:
        pedido.estadoid = Estado.objects.get(id=3)
        pedido.save()
    else:
        return redirect('gestaoPedidos:consultar_pedidos')

    if request.method == 'POST':
        form = ConfirmacaoForm(request.POST)
        if form.is_valid():
            mensagem = form.cleaned_data['mensagem']
            if mensagem:
                destinatario = 'a68033@ualg.pt'
                assunto = f'O pedido {pedido_id} encontra-se em análise.'
                mensagem = mensagem
                remetente = 'a68033@ualg.pt'
                senha = 'g!2$'
                enviar_email(destinatario, assunto, mensagem, remetente, senha)

                messages.success(request, 'Pedido em análise com sucesso')
                return redirect('gestaoPedidos:consultar_pedidos')
            else:
                messages.warning(request, 'É necessário fornecer uma mensagem para enviar o email.')
                pedido.estadoid = estado  # volta ao estado anterior
                pedido.save()
        else:
            pedido.estadoid = estado  # volta ao estado anterior
            pedido.save()
    else:
        form = ConfirmacaoForm()

    return render(request, 'gestaoPedidos/confirmacao.html', {'form': form})



def enviar_email_cp(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)

    # Verificar se o formulário foi submetido
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            # Enviar email de confirmação
            destinatario = 'diogo.raposo@live.com.pt'
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['descricao'] + f' (ID do Pedido: {pedido_id})'
            remetente = form.cleaned_data['remetente']
            senha = form.cleaned_data['senha']
            try:
                enviar_email(destinatario, assunto, mensagem, remetente, senha)
            except (SMTPAuthenticationError, UnicodeEncodeError):
                messages.error(request, 'Campos inseridos incorretamente.')
                return redirect('gestaoPedidos:consultar_pedidos')
            messages.success(request, 'Email enviado com sucesso.')
            return redirect('gestaoPedidos:consultar_pedidos')
        
    else:
        form = EmailForm()

    context = {
        'pedido': pedido,
        'form': form,
    }

    return render(request, 'gestaoPedidos/enviar_email.html', context)




@require_POST
def associar_pedido_func(request, idfunc, pedido_id):
    funcionario_id = request.POST.get('funcionario_id')
    pedido = Pedido.objects.get(id=pedido_id)
    funcionario = Funcionario.objects.get(pessoaid_id=idfunc)

    # Verifica se o funcionário responsável pelo pedido é nulo antes de atualizá-lo
    if not pedido.funcionariopessoaid:
        pedido.funcionariopessoaid = funcionario
        pedido.save()
        messages.success(request, 'Pedido associado ao funcionário com sucesso')
    else:
        messages.error(request, 'Não é possível alterar o funcionário responsável pelo pedido')
    
    return redirect('gestaoPedidos:consultar_pedidos')

def desassociar_pedido_func(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    
    try:
        funcionario = Funcionario.objects.get(pessoaid=request.user.id)
    except Funcionario.DoesNotExist:
        messages.error(request, 'Erro ao desassociar pedido. Não foi encontrado um funcionário associado ao usuário logado.')
        return redirect('gestaoPedidos:consultar_pedidos')

    if pedido.funcionariopessoaid == funcionario:
        pedido.funcionariopessoaid = None
        pedido.save()
        messages.success(request, 'Pedido desassociado do funcionário com sucesso')
    elif not pedido.funcionariopessoaid:
        messages.error(request, 'Erro ao desassociar pedido. O pedido não está associado a nenhum funcionário.')
    else:
        messages.error(request, 'Erro ao desassociar pedido. O pedido não está associado ao funcionário logado.')

    return redirect('gestaoPedidos:consultar_pedidos')

from django.shortcuts import render, redirect
from .forms import AnoLetivoForm

def criar_ano_letivo(request):
    if request.method == "POST":
        form = AnoLetivoForm(request.POST)
        if form.is_valid():
            data_inicial = form.cleaned_data['data_inicial']
            data_final = form.cleaned_data['data_final']
            
            if data_final <= data_inicial:
                messages.error(request, 'Erro ao criar Ano Letivo: data final deve ser depois da data inicial')
                return render(request, 'gestaoPedidos/criar_ano_letivo.html', {'form': form})
            
            ano_letivo = form.save(commit=False)
            conflitos = AnoLetivo.objects.filter(
                Q(data_inicial__lte=ano_letivo.data_final, data_final__gte=ano_letivo.data_inicial) | 
                Q(data_inicial__gte=ano_letivo.data_inicial, data_final__lte=ano_letivo.data_final) | 
                Q(data_inicial__lte=ano_letivo.data_inicial, data_final__gte=ano_letivo.data_final)
            )
            if conflitos.exists():
                messages.error(request, 'Erro ao criar Ano Letivo: datas conflitantes com outro ano letivo')
            else:
                ano_letivo.save()
                messages.success(request, 'Ano Letivo criado com sucesso')
                return redirect('gestaoPedidos:consultar_pedidos')
        else:
            messages.error(request, 'Erro ao criar Ano Letivo')
    else:
        form = AnoLetivoForm()
    return render(request, 'gestaoPedidos/criar_ano_letivo.html', {'form': form})

def consultar_anos_letivos(request):
    anos_letivos = AnoLetivo.objects.all()
    return render(request, 'gestaoPedidos/consultar_anos_letivos.html', {'anos_letivos': anos_letivos})

def excluir_ano_letivo(request, ano_letivo_id):
    ano_letivo = get_object_or_404(AnoLetivo, id=ano_letivo_id)
    data_inicial = ano_letivo.data_inicial
    data_final = ano_letivo.data_final

    if request.method == "POST":
        # Obter os pedidos dentro do intervalo de data do ano letivo
        pedidos_para_excluir = Pedido.objects.filter(dataAlvo__range=[data_inicial, data_final])

        # Excluir os pedidos e seus pedidos "outros" associados
        for pedido in pedidos_para_excluir:
            outro = pedido.outros
            if outro:
                outro.delete()
            pedido.delete()

        # Excluir o ano letivo
        ano_letivo.delete()

        messages.success(request, 'Ano letivo excluído com sucesso.')
        return redirect('gestaoPedidos:consultar_pedidos')

    context = {'ano_letivo': ano_letivo}
    return render(request, 'gestaoPedidos/confirmacao_de_exclusao_ano_letivo.html', context)


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
