import django_tables2 as tables
from .models import Pedido,PedidoHorario,Outros,PedidoSala,PedidoUc
from django.utils.html import format_html
from django.urls import reverse
from django.db.models import Count

class PedidosTable(tables.Table):

    id = tables.Column(order_by='id',verbose_name='Id')
    tipo = tables.Column(verbose_name='Tipo do pedido',orderable=False,empty_values=())
    estadoid = tables.Column(accessor='estadoid.descricao',verbose_name='Estado',orderable=True)
    funcionariopessoaid = tables.Column(accessor='funcionariopessoaid.pessoaid.nome',verbose_name='Funcionário',orderable=False)
    docentepessoaid = tables.Column(accessor='docentepessoaid.pessoaid.nome',verbose_name='Docente',orderable=False)
    datevalidation = tables.Column(verbose_name='Data Validação')
    datecreation = tables.Column(verbose_name='Data Criação')

    class Meta:
        model = Pedido
        sequence = ( 'id','tipo','estadoid','funcionariopessoaid','docentepessoaid','datevalidation','datecreation',)
        fields = ('id','tipo','estadoid','funcionariopessoaid','docentepessoaid','datevalidation','datecreation',)

    def render_tipo(self,record):
        if PedidoHorario.objects.filter(pedidoid=record.id).exists():
            return "Horário"
        if Outros.objects.filter(pedidoid=record.id).exists():
            return 'Outros'
        if PedidoSala.objects.filter(pedidoid=record.id).exists():
            return 'Sala'
        if PedidoUc.objects.filter(pedidoid=record.id).exists():
            return 'Uc'
        return ''
    #def order_tipo(self, queryset, is_descending):
  
    #    queryset = queryset.annotate(
    #        tipo= 
    #    ).order_by(("-" if is_descending else "") + "tipo")
    #    return (queryset, True)