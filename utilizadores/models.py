from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q
from datetime import datetime,timedelta



class Pessoa(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ucid = models.IntegerField(db_column='UCID', blank=True, null=True)  # Field name made lowercase.
    #idpedidoid22 = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='PedidoID22', blank=True, null=True)  # Field name made lowercase.
    #pedidoid2 = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='PedidoID2', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data_nascimento = models.CharField(db_column='Data_Nascimento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ativo = models.TextField(db_column='Ativo')  # Field name made lowercase. This field type is a guess.
    nacionalidade = models.IntegerField(db_column='Nacionalidade')  # Field name made lowercase.
    data_emissao_identificacao = models.CharField(db_column='Data_emissao_identificacao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data_validade_identificacao = models.CharField(db_column='Data_validade_Identificacao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nif = models.IntegerField(db_column='NIF')  # Field name made lowercase.
    pais_fiscal = models.IntegerField(db_column='Pais_Fiscal')  # Field name made lowercase.
    tipo_identificacao = models.IntegerField(db_column='Tipo_Identificacao')  # Field name made lowercase.
    digito_verificacaoo = models.SmallIntegerField(db_column='Digito_verificacaoo')  # Field name made lowercase.
    identificacao = models.CharField(db_column='Identificacao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nfunc = models.IntegerField(db_column='NFunc', blank=True, null=True)  # Field name made lowercase.
    codigo_docente = models.IntegerField(db_column='Codigo_Docente', blank=True, null=True)  # Field name made lowercase.
    departamento_docente = models.CharField(db_column='Departamento_Docente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    num_individuo = models.IntegerField(db_column='Num_Individuo', blank=True, null=True)  # Field name made lowercase.
    arquivo = models.IntegerField(db_column='Arquivo', blank=True, null=True)  # Field name made lowercase.
    discriminator = models.CharField(db_column='Discriminator', max_length=255)  # Field name made lowercase.
  
    def getProfiles(self):
        type = ''
        if Funcionario.objects.filter(utilizador_ptr_id=self):
            type = self.concat(type=type, string='Funcionario')
        if Docente.objects.filter(utilizador_ptr_id=self):
            type = self.concat(type=type, string='Docente')
        return type

    def concat(self, type, string):
        if type == '':
            type = string
        else:
            type += ', '+string
        return type

    @property
    def firstProfile(self):
        return self.getProfiles().split(' ')[0]

    def getUser(self):
        user = User.objects.get(id=self.id)
        if user.groups.filter(name = "Funcionario").exists():
            result = Funcionario.objects.get(id=self.id)
        elif user.groups.filter(name = "Docente").exists():
            result = Docente.objects.get(id=self.id)
        else:
            result = None
        return result   

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        db_table = 'pessoa'
    
    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    pessoaid = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='PessoaID')  # Field name made lowercase.

    class Meta:
        db_table = 'funcionario'

class Docente(models.Model):
    pessoaid = models.OneToOneField('Pessoa', models.DO_NOTHING, db_column='PessoaID', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'docente'

def list_to_queryset(model, data):
    from django.db.models.base import ModelBase
    if not isinstance(model, ModelBase):
        raise ValueError(
            "%s must be Model" % model
        )
    if not isinstance(data, list):
        raise ValueError(
            "%s must be List Object" % data
        )
    pk_list = [obj.pk for obj in data]
    return model.objects.filter(pk__in=pk_list)