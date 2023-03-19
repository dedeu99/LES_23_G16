from django import template
from gestaoPedidos.models import Pedido,Estado,Funcionario,Docente
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
register = template.Library()


@register.filter(name='get_descricao_estado') 
def get_descricao_estado(id):
    estado = Estado.objects.get(id=id)
    return estado.descricao


@register.filter(name='get_url_from_tipoPedido') 
def get_url_from_tipoPedido(tipo):
    if tipo == "Horário":
        return "/criar_pedido_horario"
    if tipo == "Uc":
        return "/criar_pedido_uc"
    if tipo == "Sala":
        return "/criar_pedido_sala"
    if tipo == "Outros":
        return "/criar_pedido_outros"
    return "/"

@register.filter(name='isFuncionario') 
def isFuncionario(userid):
    return Funcionario.objects.filter(id=userid).exists()