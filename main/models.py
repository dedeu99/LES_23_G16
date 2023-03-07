# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from utilizadores.models import Pessoa,Docente

class Campus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    salaid = models.ForeignKey('Sala', models.DO_NOTHING, db_column='SalaID')  # Field name made lowercase.
    gambelas = models.IntegerField(db_column='Gambelas', blank=True, null=True)  # Field name made lowercase.
    penha = models.IntegerField(db_column='Penha', blank=True, null=True)  # Field name made lowercase.
    portimao = models.IntegerField(db_column='Portimao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'campus'


class Sala(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    num = models.FloatField(db_column='Num')  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    edificio = models.IntegerField(db_column='Edificio')  # Field name made lowercase.
    campusid = models.IntegerField(db_column='Campus', blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'sala'


class Curso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codigo_curso = models.IntegerField(db_column='Codigo_Curso')  # Field name made lowercase.
    ucid = models.ForeignKey('Uc', models.DO_NOTHING, db_column='UCID')  # Field name made lowercase.

    class Meta:
        db_table = 'curso'

class DocenteUc(models.Model):
    docentepessoaid = models.OneToOneField(Docente, models.DO_NOTHING, db_column='DocentePessoaID', primary_key=True)  # Field name made lowercase.
    ucid = models.ForeignKey('Uc', models.DO_NOTHING, db_column='UCID')  # Field name made lowercase.

    class Meta:
        db_table = 'docente_uc'
        unique_together = (('docentepessoaid', 'ucid'),)


class Estado(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    criado = models.IntegerField(db_column='Criado', blank=True, null=True)  # Field name made lowercase.
    pendente = models.IntegerField(db_column='Pendente', blank=True, null=True)  # Field name made lowercase.
    aceite = models.IntegerField(db_column='Aceite', blank=True, null=True)  # Field name made lowercase.
    recusado = models.IntegerField(db_column='Recusado', blank=True, null=True)  # Field name made lowercase.
    em_espera_para_arquivar = models.IntegerField(db_column='Em espera para arquivar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eliminado = models.IntegerField(db_column='Eliminado', blank=True, null=True)  # Field name made lowercase.
    arquivado = models.IntegerField(db_column='Arquivado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'estado'


class EstadoSala(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    salaid = models.ForeignKey('Sala', models.DO_NOTHING, db_column='SalaID')  # Field name made lowercase.
    ocupada = models.IntegerField(db_column='Ocupada', blank=True, null=True)  # Field name made lowercase.
    disponivel = models.IntegerField(db_column='Disponivel', blank=True, null=True)  # Field name made lowercase.
    em_manutencao = models.IntegerField(db_column='Em_Manutencao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'estado_sala'


class Estadouc(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ucid = models.ForeignKey('Uc', models.DO_NOTHING, db_column='UCID')  # Field name made lowercase.
    ativada = models.IntegerField(db_column='Ativada', blank=True, null=True)  # Field name made lowercase.
    sem_curso = models.IntegerField(db_column='Sem curso', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    desativada = models.IntegerField(db_column='Desativada', blank=True, null=True)  # Field name made lowercase.
    sem_regente = models.IntegerField(db_column='Sem regente', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        db_table = 'estadouc'
        unique_together = (('id', 'ucid'),)






class Pedido(models.Model):
    id2 = models.AutoField(db_column='ID2', primary_key=True)  # Field name made lowercase.
    tipoalteracaoid = models.ForeignKey('Tipoalteracao', models.DO_NOTHING, db_column='TipoAlteracaoID', blank=True, null=True)  # Field name made lowercase.
    estadoid = models.ForeignKey(Estado, models.DO_NOTHING, db_column='EstadoID')  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    datecreation = models.CharField(db_column='DateCreation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    datevalidation = models.CharField(db_column='DateValidation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    criadopor = models.IntegerField(db_column='CriadoPor', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    curso = models.CharField(db_column='Curso', max_length=255, blank=True, null=True)  # Field name made lowercase.
    docenteresp = models.CharField(db_column='DocenteResp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unidadecurricular = models.IntegerField(db_column='UnidadeCurricular', blank=True, null=True)  # Field name made lowercase.
    sala = models.IntegerField(db_column='Sala', blank=True, null=True)  # Field name made lowercase.
    tipoalteracao = models.IntegerField(db_column='TipoAlteracao', blank=True, null=True)  # Field name made lowercase.
    motivopedido = models.CharField(db_column='MotivoPedido', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dataalterar = models.IntegerField(db_column='DataAlterar', blank=True, null=True)  # Field name made lowercase.
    datanova = models.IntegerField(db_column='DataNova', blank=True, null=True)  # Field name made lowercase.
    sala2 = models.IntegerField(db_column='Sala2', blank=True, null=True)  # Field name made lowercase.
    unidadec = models.IntegerField(db_column='UnidadeC', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.CharField(db_column='Data', max_length=255, blank=True, null=True)  # Field name made lowercase.
    n_mero_alunos_previstos = models.IntegerField(db_column='N�mero_alunos_previstos', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tipo_de_sala = models.IntegerField(db_column='Tipo_de_sala', blank=True, null=True)  # Field name made lowercase.
    duracao_prova = models.CharField(db_column='Duracao_prova', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discriminator = models.CharField(db_column='Discriminator', max_length=255)  # Field name made lowercase.

    class Meta:
        db_table = 'pedido'


class Horario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hora = models.DateField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    diasemana = models.CharField(db_column='DiaSemana', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'horario'


class PedidoDeHorario(models.Model):
    pedidoid2 = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='PedidoID2', primary_key=True)  # Field name made lowercase.
    #horarioantigoid = models.ForeignKey(Horario, models.DO_NOTHING, db_column='HorarioAntigo')  # Field name made lowercase.
    #horarionovoid = models.ForeignKey(Horario, models.DO_NOTHING, db_column='HorarioNovo')  # Field name made lowercase.

    class Meta:
        db_table = 'pedido_de_horario'
        unique_together = (('pedidoid2'),)#, 'horarioantigoid', 'horarionovoid'),)


class PedidoDeOutros(models.Model):
    pedidoid2 = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='PedidoID2', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'pedido_de_outros'


class PedidoDeSala(models.Model):
    pedidoid2 = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='PedidoID2', primary_key=True)  # Field name made lowercase.
    salaid = models.ForeignKey('Sala', models.DO_NOTHING, db_column='SalaID')  # Field name made lowercase.

    class Meta:
        db_table = 'pedido_de_sala'
        unique_together = (('pedidoid2', 'salaid'),)


class PedidoDeUc(models.Model):
    pedidoid2 = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='PedidoID2', primary_key=True)  # Field name made lowercase.
    ucid = models.ForeignKey('Uc', models.DO_NOTHING, db_column='UCID')  # Field name made lowercase.

    class Meta:
        db_table = 'pedido_de_uc'



class TipoSala(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    salaid = models.ForeignKey(Sala, models.DO_NOTHING, db_column='SalaID')  # Field name made lowercase.
    computadores = models.IntegerField(db_column='Computadores', blank=True, null=True)  # Field name made lowercase.
    vdi = models.IntegerField(db_column='VDI', blank=True, null=True)  # Field name made lowercase.
    normal = models.IntegerField(db_column='Normal', blank=True, null=True)  # Field name made lowercase.
    laboratorio = models.IntegerField(db_column='Laboratorio', blank=True, null=True)  # Field name made lowercase.
    anfiteatro = models.IntegerField(db_column='Anfiteatro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tipo_sala'


class Tipoalteracao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pontual = models.IntegerField(db_column='Pontual', blank=True, null=True)  # Field name made lowercase.
    permanente = models.IntegerField(db_column='Permanente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tipoalteracao'


class Uc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    semestrelecionada = models.IntegerField(db_column='SemestreLecionada')  # Field name made lowercase.
    codigo_disciplina = models.IntegerField(db_column='Codigo_disciplina')  # Field name made lowercase.
    nomeuc = models.CharField(db_column='NomeUC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inst_disciplina = models.CharField(db_column='Inst_disciplina', max_length=255, blank=True, null=True)  # Field name made lowercase.
    turma = models.CharField(db_column='Turma', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cursos = models.IntegerField(db_column='Cursos', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    regente = models.IntegerField(db_column='Regente', blank=True, null=True)  # Field name made lowercase.
    anolecionada = models.IntegerField(db_column='AnoLecionada')  # Field name made lowercase.
    horas_semanais = models.CharField(db_column='Horas_semanais', max_length=255, blank=True, null=True)  # Field name made lowercase.
    horas_periodo = models.CharField(db_column='Horas_Periodo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data_inicio = models.CharField(db_column='Data_Inicio', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data_fim = models.CharField(db_column='Data_Fim', max_length=255, blank=True, null=True)  # Field name made lowercase.