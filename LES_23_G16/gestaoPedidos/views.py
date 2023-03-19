from django.shortcuts import render
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from .tables import PedidosTable
from .filters import PedidosFilter
#from django.core.paginator import Paginator
from .models import Pedido
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
    return render(request=request,
                template_name="gestaoPedidos/criar_pedido_horario.html")