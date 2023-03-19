import django_tables2 as tables
from .models import Pedido,PedidoHorario,Outros,PedidoSala,PedidoUc
from django.utils.html import format_html
from django.urls import reverse
from django.db.models import Count

class PedidosTable(tables.Table):

    id = tables.Column(order_by='id',verbose_name='Id')
    tipo = tables.Column(accessor='get_tipo_pedido',verbose_name='Tipo do pedido',orderable=False)
    estadoid = tables.Column(accessor='estadoid.descricao',verbose_name='Estado',orderable=True)
    funcionariopessoaid = tables.Column(accessor='funcionariopessoaid.pessoaid.nome',verbose_name='Funcionário',orderable=False)
    docentepessoaid = tables.Column(accessor='docentepessoaid.pessoaid.nome',verbose_name='Docente',orderable=False)
    datevalidation = tables.Column(verbose_name='Data Validação')
    datecreation = tables.Column(verbose_name='Data Criação')

    class Meta:
        model = Pedido
        sequence = ( 'id','tipo','estadoid','funcionariopessoaid','docentepessoaid','datevalidation','datecreation',)
        #exclude = ('datecreation', )
        fields = ('id','tipo','estadoid','funcionariopessoaid','docentepessoaid','datevalidation','datecreation',)

    #def teste(self,a,b,c,d):
    #    if a>0:
    #        return 1
    #    if b>0:
    #        return 2
    #    if c>0:
    #        return 3
    #    if d>0:
    #        return 4
    #    return -1
    
    #def order_tipo(self, queryset, is_descending):
  
    #    queryset = queryset.annotate(
    #        tipo= self.teste(Count("pedidohorario").output_field.,Count("pedidouc").output_field,Count("pedidosala").output_field,Count("outros").output_field)
    #    ).order_by(("-" if is_descending else "") + "tipo")
    #    return (queryset, True)