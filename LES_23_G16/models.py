# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Campus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'campus'


class Curso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    codigo_curso = models.IntegerField(db_column='Codigo_Curso')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'curso'


class CursoUc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cursoid = models.OneToOneField(Curso, models.DO_NOTHING, db_column='CursoID')  # Field name made lowercase.
    ucid = models.OneToOneField('Uc', models.DO_NOTHING, db_column='UCID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'curso_uc'
        unique_together = (('cursoid', 'ucid'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Docente(models.Model):
    codigo_docente = models.IntegerField(db_column='Codigo_Docente')  # Field name made lowercase.
    departamento_docente = models.CharField(db_column='Departamento_Docente', max_length=255)  # Field name made lowercase.
    num_individuo = models.IntegerField(db_column='Num_Individuo')  # Field name made lowercase.
    arquivo = models.TextField(db_column='Arquivo')  # Field name made lowercase.
    pessoaid = models.OneToOneField('Pessoa', models.DO_NOTHING, db_column='PessoaID', primary_key=True)  # Field name made lowercase.
    cursoid = models.ForeignKey(Curso, models.DO_NOTHING, db_column='CursoID')  # Field name made lowercase.
    ucid = models.ForeignKey('Uc', models.DO_NOTHING, db_column='UCID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'docente'


class Estado(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado'


class EstadoSala(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado_sala'


class Estadouc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.
    ucid = models.ForeignKey('Uc', models.DO_NOTHING, db_column='UCID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estadouc'


class Funcionario(models.Model):
    nfunc = models.IntegerField(db_column='NFunc')  # Field name made lowercase.
    pessoaid = models.OneToOneField('Pessoa', models.DO_NOTHING, db_column='PessoaID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'funcionario'


class Horario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hora = models.DateField(db_column='Hora')  # Field name made lowercase.
    diasemana = models.CharField(db_column='DiaSemana', max_length=255)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'horario'


class Outros(models.Model):
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.
    data = models.CharField(db_column='Data', max_length=255)  # Field name made lowercase.
    numero_alunos_previstos = models.IntegerField(db_column='Numero_alunos_previstos')  # Field name made lowercase.
    duracao_prova = models.CharField(db_column='Duracao_prova', max_length=255)  # Field name made lowercase.
    pedidoid = models.OneToOneField('Pedido', models.DO_NOTHING, db_column='PedidoID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'outros'


class Pedido(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dataalvo = models.DateField(db_column='dataAlvo')  # Field name made lowercase.
    assunto = models.CharField(max_length=255)
    descricao = models.TextField()
    datecreation = models.DateField(db_column='DateCreation')  # Field name made lowercase.
    datevalidation = models.DateField(db_column='DateValidation', blank=True, null=True)  # Field name made lowercase.
    estadoid = models.ForeignKey(Estado, models.DO_NOTHING, db_column='EstadoID')  # Field name made lowercase.
    docentepessoaid = models.ForeignKey(Docente, models.DO_NOTHING, db_column='DocentePessoaID')  # Field name made lowercase.
    funcionariopessoaid = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='FuncionarioPessoaID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pedido'


class PedidoHorario(models.Model):
    motivopedido = models.CharField(db_column='MotivoPedido', max_length=255)  # Field name made lowercase.
    dataalterar = models.IntegerField(db_column='DataAlterar')  # Field name made lowercase.
    datanova = models.IntegerField(db_column='DataNova')  # Field name made lowercase.
    pedidoid = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='PedidoID', primary_key=True)  # Field name made lowercase.
    horarioid = models.ForeignKey(Horario, models.DO_NOTHING, db_column='HorarioID')  # Field name made lowercase.
    horarioid2 = models.ForeignKey(Horario, models.DO_NOTHING, db_column='HorarioID2')  # Field name made lowercase.
    tipoalteracaoid = models.ForeignKey('Tipoalteracao', models.DO_NOTHING, db_column='TipoAlteracaoID')  # Field name made lowercase.
    unidadec = models.ForeignKey('Uc', models.DO_NOTHING, db_column='UnidadeC')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pedido_horario'


class PedidoSala(models.Model):
    pedidoid = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='PedidoID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pedido_sala'


class PedidoUc(models.Model):
    pedidoid = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='PedidoID', primary_key=True)  # Field name made lowercase.
    motivopedido = models.CharField(db_column='MotivoPedido', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dataalterar = models.IntegerField(db_column='DataAlterar', blank=True, null=True)  # Field name made lowercase.
    datanova = models.IntegerField(db_column='DataNova', blank=True, null=True)  # Field name made lowercase.
    id_uc = models.IntegerField(blank=True, null=True)
    semestrelecionada = models.CharField(db_column='SemestreLecionada', max_length=255)  # Field name made lowercase.
    nomeuc = models.CharField(db_column='NomeUC', max_length=255)  # Field name made lowercase.
    anolecionada = models.CharField(db_column='AnoLecionada', max_length=255)  # Field name made lowercase.
    horas_semanais = models.CharField(db_column='Horas_semanais', max_length=255)  # Field name made lowercase.
    horas_periodo = models.CharField(db_column='Horas_Periodo', max_length=255)  # Field name made lowercase.
    data_inicio = models.CharField(db_column='Data_Inicio', max_length=255)  # Field name made lowercase.
    regente = models.CharField(db_column='Regente', max_length=255)  # Field name made lowercase.
    data_fim = models.CharField(db_column='Data_Fim', max_length=255)  # Field name made lowercase.
    curso = models.CharField(db_column='Curso', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pedido_uc'


class Pessoa(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=255)  # Field name made lowercase.
    data_nascimento = models.CharField(db_column='Data_Nascimento', max_length=255)  # Field name made lowercase.
    ativo = models.TextField(db_column='Ativo')  # Field name made lowercase.
    nacionalidade = models.IntegerField(db_column='Nacionalidade')  # Field name made lowercase.
    data_emissao_identificacao = models.CharField(db_column='Data_emissao_identificacao', max_length=255)  # Field name made lowercase.
    data_validade_identificacao = models.CharField(db_column='Data_validade_Identificacao', max_length=255)  # Field name made lowercase.
    nif = models.IntegerField(db_column='NIF')  # Field name made lowercase.
    pais_fiscal = models.IntegerField(db_column='Pais_Fiscal')  # Field name made lowercase.
    tipo_identificacao = models.IntegerField(db_column='Tipo_Identificacao')  # Field name made lowercase.
    digito_verificacao = models.SmallIntegerField(db_column='Digito_verificacao')  # Field name made lowercase.
    identificacao = models.CharField(db_column='Identificacao', max_length=255)  # Field name made lowercase.
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pessoa'


class Sala(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    num = models.FloatField(db_column='Num')  # Field name made lowercase.
    edificio = models.IntegerField(db_column='Edificio')  # Field name made lowercase.
    campusid = models.ForeignKey(Campus, models.DO_NOTHING, db_column='CampusID')  # Field name made lowercase.
    estado_salaid = models.ForeignKey(EstadoSala, models.DO_NOTHING, db_column='Estado_SalaID')  # Field name made lowercase.
    tipo_salaid = models.ForeignKey('TipoSala', models.DO_NOTHING, db_column='Tipo_SalaID')  # Field name made lowercase.
    pedido_salapedidoid = models.ForeignKey(PedidoSala, models.DO_NOTHING, db_column='Pedido_SalaPedidoID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sala'


class TipoSala(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_sala'


class Tipoalteracao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipoalteracao'


class Uc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    semestrelecionada = models.IntegerField(db_column='SemestreLecionada')  # Field name made lowercase.
    codigo_disciplina = models.IntegerField(db_column='Codigo_disciplina')  # Field name made lowercase.
    nomeuc = models.CharField(db_column='NomeUC', max_length=255)  # Field name made lowercase.
    inst_disciplina = models.CharField(db_column='Inst_disciplina', max_length=255)  # Field name made lowercase.
    turma = models.CharField(db_column='Turma', max_length=255)  # Field name made lowercase.
    anolecionada = models.IntegerField(db_column='AnoLecionada')  # Field name made lowercase.
    horas_semanais = models.CharField(db_column='Horas_semanais', max_length=255)  # Field name made lowercase.
    horas_periodo = models.CharField(db_column='Horas_Periodo', max_length=255)  # Field name made lowercase.
    data_inicio = models.CharField(db_column='Data_Inicio', max_length=255)  # Field name made lowercase.
    data_fim = models.CharField(db_column='Data_Fim', max_length=255)  # Field name made lowercase.
    pedido_ucpedidoid = models.ForeignKey(PedidoUc, models.DO_NOTHING, db_column='Pedido_UCPedidoID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'uc'
