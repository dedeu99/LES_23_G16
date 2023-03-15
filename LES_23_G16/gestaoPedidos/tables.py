import django_tables2 as django_tables
from .models import Pedido
from django.utils.html import format_html
from django.urls import reverse


class PedidosTable(django_tables.Table):

    id = django_tables.Column(
        empty_values=(), order_by=("ID"))#, order_by=("first_name", "last_name"))
    estado = django_tables.Column(
        'Estado')
    
    class Meta:
        model = Pedido
        #sequence = ('ID', 'EstadoID')
        fields = ("ID","EstadoID", )

    def before_render(self, request):
        self.columns.hide('id')
        self.columns.hide('estado')

    def render_id(self, record):
        return f"{record.ID}"

    def render_estado(self, record):
        return f"{record.EstadoID}"