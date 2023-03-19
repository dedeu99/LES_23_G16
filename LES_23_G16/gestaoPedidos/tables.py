import django_tables2 as tables
from .models import Pedido,PedidoHorario,Outros,PedidoSala,PedidoUc

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
    
    #def before_render(self, request):
    #    self.table_data = Pedido.objects.filter(funcionariopessoaid = request.user.id)
    #    self.rows.data.
        #if request.user.has_perm('foo.delete_bar'):
        #    self.rows.sh
        #else:
        #    self.columns.show('country')
    #def order_tipo(self, queryset, is_descending):
  
    #    queryset = queryset.annotate(
    #        tipo= 
    #    ).order_by(("-" if is_descending else "") + "tipo")
    #    return (queryset, True)
    #def dispatch(self, request, *args, **kwargs):
    #    """Updates the keyword args to always have 'foo' with the value 'bar'"""
    #    if request.:
    #    # Block requests that attempt to provide their own foo value
    #        return HttpResponse(status_code=400)
    #    kwargs.update({'foo': 'bar'}) # inject the foo value
    #    # now process dispatch as it otherwise normally would
    #    return super().dispatch(request, *args, **kwargs)