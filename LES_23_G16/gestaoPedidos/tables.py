import django_tables2 as tables
from .models import Pedido
from django.utils.html import format_html
from django.urls import reverse


class PedidosTable(tables.Table):

    id = tables.Column(order_by='id',verbose_name='Id')
    tipo = tables.Column(accessor='get_tipo_pedido',verbose_name='Tipo do pedido')
    estadoid = tables.Column(accessor='estadoid.descricao',verbose_name='Estado',orderable=True)
    funcionariopessoaid = tables.Column(accessor='funcionariopessoaid.pessoaid.nome',verbose_name='Funcionário',orderable=True)
    docentepessoaid = tables.Column(accessor='docentepessoaid.pessoaid.nome',verbose_name='Docente')
    datevalidation = tables.Column(verbose_name='Data Validação')
    datecreation = tables.Column(verbose_name='Data Criação')

    class Meta:
        model = Pedido
        sequence = ( 'id','tipo','estadoid','funcionariopessoaid','docentepessoaid','datevalidation','datecreation')
        #exclude = ('datecreation', )
        #fields = ['id','tipo','estadoid','funcionariopessoaid','docentepessoaid','datevalidation','datecreation']

    #def before_render(self, request):
        #self.columns.hide('id')
        #self.columns.hide('estado')

#    render_id(self, record):
#        return f"{record.ID}"

    #def order(self, queryset, is_descending):
    #        queryset = queryset.annotate(
    #        amount=F("shirts") + F("pants")
    #    ).order_by(("-" if is_descending else "") + "amount")
    #    return (queryset, True)