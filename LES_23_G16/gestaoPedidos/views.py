from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from .tables import PedidosTable
from .filters import PedidosFilter
#from django.core.paginator import Paginator
from .models import Pedido,PedidoHorario,Docente,Estado
from .forms import PedidoForm,PedidoHorarioForm
from django.shortcuts import HttpResponse
import datetime
from django.views.decorators.http import require_POST
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
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
