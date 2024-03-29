# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Campus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'campus'


class Curso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    codigo_curso = models.IntegerField(db_column='Codigo_Curso')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'curso'


class Docente(models.Model):
    codigo_docente = models.IntegerField(db_column='Codigo_Docente')  # Field name made lowercase.
    departamento_docente = models.CharField(db_column='Departamento_Docente', max_length=255)  # Field name made lowercase.
    num_individuo = models.IntegerField(db_column='Num_Individuo')  # Field name made lowercase.
    arquivo = models.TextField(db_column='Arquivo')  # Field name made lowercase. This field type is a guess.
    pessoaid = models.OneToOneField('Pessoa', models.DO_NOTHING, db_column='PessoaID', primary_key=True)  # Field name made lowercase.
    cursoid = models.ForeignKey(Curso, models.DO_NOTHING, db_column='CursoID')  # Field name made lowercase.
    ucid = models.ForeignKey('Uc', models.DO_NOTHING, db_column='UCID', null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'docente'

    def __str__(self):
        return str(self.codigo_docente)

class Estado(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'estado'

    def __str__(self):
        return self.descricao

class EstadoSala(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'estado_sala'


class Estadouc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ucid = models.ForeignKey('Uc', models.DO_NOTHING, db_column='UCID')  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'estadouc'


class Funcionario(models.Model):
    nfunc = models.IntegerField(db_column='NFunc')  # Field name made lowercase.
    pessoaid = models.OneToOneField('Pessoa', models.DO_NOTHING, db_column='PessoaID', primary_key=True)  # Field name made lowercase.
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    class Meta:
        managed = True
        db_table = 'funcionario'


class Horario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hora = models.DateField(db_column='Hora')  # Field name made lowercase.
    diasemana = models.CharField(db_column='DiaSemana', max_length=255)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'horario'


class Outros(models.Model):
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.
    data = models.CharField(db_column='Data', max_length=255)  # Field name made lowercase.
    numero_alunos_previstos = models.IntegerField(db_column='Numero_alunos_previstos')  # Field name made lowercase.
    duracao_prova = models.CharField(db_column='Duracao_prova', max_length=255)  # Field name made lowercase.
    pedidoid = models.OneToOneField('Pedido', models.DO_NOTHING, db_column='PedidoID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'outros'

class Tipoalteracao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tipoalteracao'
    def __str__(self):
        return self.descricao

class Pedido(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dataAlvo = models.DateField(db_column='dataAlvo',verbose_name="Data Alvo")
    assunto = models.CharField(db_column='assunto', max_length=255,verbose_name="Assunto")
    descricao = models.TextField(db_column='descricao', max_length=255,verbose_name="Descrição")
    estadoid = models.ForeignKey(Estado, models.DO_NOTHING, db_column='EstadoID',verbose_name="Estado")  # Field name made lowercase.
    funcionariopessoaid = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='FuncionarioPessoaID', null=True)  # Field name made lowercase.
    docentepessoaid = models.ForeignKey(Docente, models.DO_NOTHING, db_column='DocentePessoaID')  # Field name made lowercase.
    datecreation = models.DateField(db_column='DateCreation')  
    datevalidation = models.DateField(db_column='DateValidation', null=True)
    class Meta:
        managed = True
        db_table = 'pedido'


        
class PedidoUC(models.Model):
    nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    curso = models.CharField(db_column='Curso', max_length=255)  # Field name made lowercase.
    docenteresp = models.CharField(db_column='DocenteResp', max_length=255)  # Field name made lowercase.
    pedidoid = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='PedidoID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'pedido_uc'


class UC(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    pedido_uc = models.ForeignKey(PedidoUC, models.DO_NOTHING, db_column='Pedido_UCPedidoID')
    semestre_lecionada = models.IntegerField(db_column='SemestreLecionada')
    codigo_disciplina = models.IntegerField(db_column='Codigo_disciplina')
    nomeuc = models.CharField(db_column='NomeUC', max_length=255)
    instituicao_disciplina = models.CharField(db_column='Inst_disciplina', max_length=255)
    turma = models.CharField(db_column='Turma', max_length=255)
    ano_lecionada = models.IntegerField(db_column='AnoLecionada')
    horas_semanais = models.CharField(db_column='Horas_semanais', max_length=255)
    horas_periodo = models.CharField(db_column='Horas_Periodo', max_length=255)
    data_inicio = models.CharField(db_column='Data_Inicio', max_length=255)
    data_fim = models.CharField(db_column='Data_Fim', max_length=255)

    class Meta:
        managed = True
        db_table = 'uc'
    def __str__(self):
        return self.nomeuc
    

class PedidoHorario(models.Model):
    motivopedido = models.CharField(db_column='MotivoPedido', max_length=255,verbose_name="Motivo do Pedido")  # Field name made lowercase.
    dataalterar = models.IntegerField(db_column='DataAlterar')  # Field name made lowercase.
    datanova = models.IntegerField(db_column='DataNova')  # Field name made lowercase.
    #sala = models.IntegerField(db_column='Sala')  # Field name made lowercase.
    unidadec = models.ForeignKey(UC,models.DO_NOTHING,db_column='UnidadeC',verbose_name="Unidade Curricular")  # Field name made lowercase.
    pedidoid = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='PedidoID', primary_key=True)  # Field name made lowercase.
    horarioid2 = models.ForeignKey(Horario, models.DO_NOTHING, db_column='HorarioID2', related_name='horarioid2')  # Field name made lowercase.
    tipoalteracaoid = models.ForeignKey(Tipoalteracao, models.DO_NOTHING, db_column='TipoAlteracaoID',verbose_name="Tipo de Alteração")  # Field name made lowercase.
    horarioid = models.ForeignKey(Horario, models.DO_NOTHING, db_column='HorarioID', related_name='horarioid')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'pedido_horario'


class PedidoSala(models.Model):
    pedidoid = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='PedidoID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'pedido_sala'

class Pessoa(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=255)  # Field name made lowercase.
    data_nascimento = models.CharField(db_column='Data_Nascimento', max_length=255)  # Field name made lowercase.
    ativo = models.TextField(db_column='Ativo')  # Field name made lowercase. This field type is a guess.
    nacionalidade = models.IntegerField(db_column='Nacionalidade')  # Field name made lowercase.
    data_emissao_identificacao = models.CharField(db_column='Data_emissao_identificacao', max_length=255)  # Field name made lowercase.
    data_validade_identificacao = models.CharField(db_column='Data_validade_Identificacao', max_length=255)  # Field name made lowercase.
    nif = models.IntegerField(db_column='NIF')  # Field name made lowercase.
    pais_fiscal = models.IntegerField(db_column='Pais_Fiscal')  # Field name made lowercase.
    tipo_identificacao = models.IntegerField(db_column='Tipo_Identificacao')  # Field name made lowercase.
    digito_verificacao = models.SmallIntegerField(db_column='Digito_verificacao')  # Field name made lowercase.
    identificacao = models.CharField(db_column='Identificacao', max_length=255)  # Field name made lowercase.
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='user',default=None, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'pessoa'


class Sala(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    estado_salaid = models.ForeignKey(EstadoSala, models.DO_NOTHING, db_column='Estado_SalaID')  # Field name made lowercase.
    tipo_salaid = models.ForeignKey('TipoSala', models.DO_NOTHING, db_column='Tipo_SalaID')  # Field name made lowercase.
    campusid = models.ForeignKey(Campus, models.DO_NOTHING, db_column='CampusID')  # Field name made lowercase.
    pedido_salapedidoid = models.ForeignKey(PedidoSala, models.DO_NOTHING, db_column='Pedido_SalaPedidoID')  # Field name made lowercase.
    num = models.FloatField(db_column='Num')  # Field name made lowercase.
    edificio = models.IntegerField(db_column='Edificio')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'sala'


class TipoSala(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tipo_sala'



class CursoUc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cursoid = models.OneToOneField(Curso, models.DO_NOTHING, db_column='CursoID')  # Field name made lowercase.
    ucid = models.OneToOneField(UC, models.DO_NOTHING, db_column='UCID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'curso_uc'
        unique_together = (('cursoid', 'ucid'))
        

class AnoLetivo(models.Model):
    nome = models.CharField(db_column='Nome', max_length=255)
    data_inicial = models.DateField(db_column='DataInicial')
    data_final = models.DateField(db_column='DataFinal')

    class Meta:
        managed = True
        db_table = 'ano_letivo'
