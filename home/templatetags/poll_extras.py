from django import template
from gestaoPedidos.models import Pessoa,Estado,Funcionario,Docente,PedidoHorario
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
register = template.Library()


@register.filter(name='get_nome') 
def get_nome(id):
    pessoa = Pessoa.objects.get(id=id)
    return pessoa.nome
@register.filter(name='get_descricao_estado') 
def get_descricao_estado(id):
    estado = Estado.objects.get(id=id)
    return estado.descricao


@register.filter(name='get_create_url_from_tipoPedido') 
def get_create_url_from_tipoPedido(tipo):
    if tipo == "Horário":
        return "/criar_pedido_horario"
    if tipo == "Uc":
        return "/criar_pedido_uc"
    if tipo == "Sala":
        return "/criar_pedido_sala"
    if tipo == "Outros":
        return "/criar_pedido_outros"
    return "#"

@register.filter(name='isFuncionario') 
def isFuncionario(userid):
    pessoa=Pessoa.objects.get(id=userid)
    if pessoa:
        return Funcionario.objects.filter(pessoaid=pessoa.id).exists()
    
@register.filter(name='get_delete_url_from_tipoPedido') 
def get_delete_url_from_tipoPedido(tipo,id):
    if tipo == "Horário":
        return str("apagar_pedido_horario?id={}").format(id)
    if tipo == "Uc":
        return str("apagar_pedido_uc?id={}").format(id)
    if tipo == "Sala":
        return str("apagar_pedido_sala?id={}").format(id)
    if tipo == "Outros":
        return str("apagar_pedido_outros?id={}").format(id)
    return "#"


@register.filter(name='get_alter_url_from_tipoPedido') 
def get_alter_url_from_tipoPedido(tipo,id):
    if tipo == "Horário":
        return str("alterar_pedido_horario?id={}").format(id)
    if tipo == "Uc":
         return str("alterar_pedido_uc?id={}").format(id)
    if tipo == "Sala":
         return str("alterar_pedido_sala?id={}").format(id)
    if tipo == "Outros":
         return str("alterar_pedido_outros?id={}").format(id)
    return "#"


@register.filter(name='get_tipo_alteracao') 
def get_tipo_alteracao(id):
    if PedidoHorario.objects.filter(pedidoid=id).exists():
        return PedidoHorario.objects.get(pedidoid=id).tipoalteracaoid
    else:
        return 'ERRO'


@register.filter(name='get_unidade_curricular') 
def get_unidade_curricular(id):
    if PedidoHorario.objects.filter(pedidoid=id).exists():
        return PedidoHorario.objects.get(pedidoid=id).unidadec
    else:
        return 'ERRO'