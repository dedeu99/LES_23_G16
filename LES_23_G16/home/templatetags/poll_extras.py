from django import template
from gestaoPedidos.models import Pedido,Estado
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
register = template.Library()


@register.filter(name='get_descricao_estado') 
def get_descricao_estado(id):
    estado = Estado.objects.get(id=id)
    return estado.descricao
