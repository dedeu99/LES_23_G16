# Generated by Django 4.1.7 on 2023-03-04 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('criado', models.IntegerField(blank=True, db_column='Criado', null=True)),
                ('pendente', models.IntegerField(blank=True, db_column='Pendente', null=True)),
                ('aceite', models.IntegerField(blank=True, db_column='Aceite', null=True)),
                ('recusado', models.IntegerField(blank=True, db_column='Recusado', null=True)),
                ('em_espera_para_arquivar', models.IntegerField(blank=True, db_column='Em espera para arquivar', null=True)),
                ('eliminado', models.IntegerField(blank=True, db_column='Eliminado', null=True)),
                ('arquivado', models.IntegerField(blank=True, db_column='Arquivado', null=True)),
            ],
            options={
                'db_table': 'estado',
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('hora', models.DateField(blank=True, db_column='Hora', null=True)),
                ('diasemana', models.CharField(blank=True, db_column='DiaSemana', max_length=255, null=True)),
                ('descricao', models.CharField(blank=True, db_column='Descricao', max_length=255, null=True)),
            ],
            options={
                'db_table': 'horario',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id2', models.AutoField(db_column='ID2', primary_key=True, serialize=False)),
                ('estado', models.IntegerField(blank=True, db_column='Estado', null=True)),
                ('id', models.IntegerField(db_column='Id')),
                ('datecreation', models.CharField(blank=True, db_column='DateCreation', max_length=255, null=True)),
                ('datevalidation', models.CharField(blank=True, db_column='DateValidation', max_length=255, null=True)),
                ('criadopor', models.IntegerField(blank=True, db_column='CriadoPor', null=True)),
                ('nome', models.CharField(blank=True, db_column='Nome', max_length=255, null=True)),
                ('curso', models.CharField(blank=True, db_column='Curso', max_length=255, null=True)),
                ('docenteresp', models.CharField(blank=True, db_column='DocenteResp', max_length=255, null=True)),
                ('unidadecurricular', models.IntegerField(blank=True, db_column='UnidadeCurricular', null=True)),
                ('sala', models.IntegerField(blank=True, db_column='Sala', null=True)),
                ('tipoalteracao', models.IntegerField(blank=True, db_column='TipoAlteracao', null=True)),
                ('motivopedido', models.CharField(blank=True, db_column='MotivoPedido', max_length=255, null=True)),
                ('dataalterar', models.IntegerField(blank=True, db_column='DataAlterar', null=True)),
                ('datanova', models.IntegerField(blank=True, db_column='DataNova', null=True)),
                ('sala2', models.IntegerField(blank=True, db_column='Sala2', null=True)),
                ('unidadec', models.IntegerField(blank=True, db_column='UnidadeC', null=True)),
                ('descricao', models.CharField(blank=True, db_column='Descricao', max_length=255, null=True)),
                ('data', models.CharField(blank=True, db_column='Data', max_length=255, null=True)),
                ('n_mero_alunos_previstos', models.IntegerField(blank=True, db_column='N�mero_alunos_previstos', null=True)),
                ('tipo_de_sala', models.IntegerField(blank=True, db_column='Tipo_de_sala', null=True)),
                ('duracao_prova', models.CharField(blank=True, db_column='Duracao_prova', max_length=255, null=True)),
                ('discriminator', models.CharField(db_column='Discriminator', max_length=255)),
                ('estadoid', models.ForeignKey(db_column='EstadoID', on_delete=django.db.models.deletion.DO_NOTHING, to='main.estado')),
            ],
            options={
                'db_table': 'pedido',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('ucid', models.IntegerField(blank=True, db_column='UCID', null=True)),
                ('nome', models.CharField(blank=True, db_column='Nome', max_length=255, null=True)),
                ('sexo', models.CharField(blank=True, db_column='Sexo', max_length=255, null=True)),
                ('data_nascimento', models.CharField(blank=True, db_column='Data_Nascimento', max_length=255, null=True)),
                ('ativo', models.TextField(db_column='Ativo')),
                ('nacionalidade', models.IntegerField(db_column='Nacionalidade')),
                ('data_emissao_identificacao', models.CharField(blank=True, db_column='Data_emissao_identificacao', max_length=255, null=True)),
                ('data_validade_identificacao', models.CharField(blank=True, db_column='Data_validade_Identificacao', max_length=255, null=True)),
                ('nif', models.IntegerField(db_column='NIF')),
                ('pais_fiscal', models.IntegerField(db_column='Pais_Fiscal')),
                ('tipo_identificacao', models.IntegerField(db_column='Tipo_Identificacao')),
                ('digito_verificacaoo', models.SmallIntegerField(db_column='Digito_verificacaoo')),
                ('identificacao', models.CharField(blank=True, db_column='Identificacao', max_length=255, null=True)),
                ('nfunc', models.IntegerField(blank=True, db_column='NFunc', null=True)),
                ('codigo_docente', models.IntegerField(blank=True, db_column='Codigo_Docente', null=True)),
                ('departamento_docente', models.CharField(blank=True, db_column='Departamento_Docente', max_length=255, null=True)),
                ('num_individuo', models.IntegerField(blank=True, db_column='Num_Individuo', null=True)),
                ('arquivo', models.IntegerField(blank=True, db_column='Arquivo', null=True)),
                ('discriminator', models.CharField(db_column='Discriminator', max_length=255)),
            ],
            options={
                'db_table': 'pessoa',
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('num', models.FloatField(db_column='Num')),
                ('estado', models.IntegerField(blank=True, db_column='Estado', null=True)),
                ('edificio', models.IntegerField(db_column='Edificio')),
                ('campusid', models.IntegerField(blank=True, db_column='Campus', null=True)),
                ('tipo', models.IntegerField(blank=True, db_column='Tipo', null=True)),
            ],
            options={
                'db_table': 'sala',
            },
        ),
        migrations.CreateModel(
            name='Tipoalteracao',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('pontual', models.IntegerField(blank=True, db_column='Pontual', null=True)),
                ('permanente', models.IntegerField(blank=True, db_column='Permanente', null=True)),
            ],
            options={
                'db_table': 'tipoalteracao',
            },
        ),
        migrations.CreateModel(
            name='Uc',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('semestrelecionada', models.IntegerField(db_column='SemestreLecionada')),
                ('codigo_disciplina', models.IntegerField(db_column='Codigo_disciplina')),
                ('nomeuc', models.CharField(blank=True, db_column='NomeUC', max_length=255, null=True)),
                ('inst_disciplina', models.CharField(blank=True, db_column='Inst_disciplina', max_length=255, null=True)),
                ('turma', models.CharField(blank=True, db_column='Turma', max_length=255, null=True)),
                ('cursos', models.IntegerField(blank=True, db_column='Cursos', null=True)),
                ('estado', models.IntegerField(blank=True, db_column='Estado', null=True)),
                ('regente', models.IntegerField(blank=True, db_column='Regente', null=True)),
                ('anolecionada', models.IntegerField(db_column='AnoLecionada')),
                ('horas_semanais', models.CharField(blank=True, db_column='Horas_semanais', max_length=255, null=True)),
                ('horas_periodo', models.CharField(blank=True, db_column='Horas_Periodo', max_length=255, null=True)),
                ('data_inicio', models.CharField(blank=True, db_column='Data_Inicio', max_length=255, null=True)),
                ('data_fim', models.CharField(blank=True, db_column='Data_Fim', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('pessoaid', models.OneToOneField(db_column='PessoaID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.pessoa')),
            ],
            options={
                'db_table': 'docente',
            },
        ),
        migrations.CreateModel(
            name='PedidoDeOutros',
            fields=[
                ('pedidoid2', models.OneToOneField(db_column='PedidoID2', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.pedido')),
            ],
            options={
                'db_table': 'pedido_de_outros',
            },
        ),
        migrations.CreateModel(
            name='TipoSala',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('computadores', models.IntegerField(blank=True, db_column='Computadores', null=True)),
                ('vdi', models.IntegerField(blank=True, db_column='VDI', null=True)),
                ('normal', models.IntegerField(blank=True, db_column='Normal', null=True)),
                ('laboratorio', models.IntegerField(blank=True, db_column='Laboratorio', null=True)),
                ('anfiteatro', models.IntegerField(blank=True, db_column='Anfiteatro', null=True)),
                ('salaid', models.ForeignKey(db_column='SalaID', on_delete=django.db.models.deletion.DO_NOTHING, to='main.sala')),
            ],
            options={
                'db_table': 'tipo_sala',
            },
        ),
        migrations.AddField(
            model_name='pedido',
            name='tipoalteracaoid',
            field=models.ForeignKey(blank=True, db_column='TipoAlteracaoID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.tipoalteracao'),
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoaid', models.ForeignKey(db_column='PessoaID', on_delete=django.db.models.deletion.DO_NOTHING, to='main.pessoa')),
            ],
            options={
                'db_table': 'funcionario',
            },
        ),
        migrations.CreateModel(
            name='EstadoSala',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('ocupada', models.IntegerField(blank=True, db_column='Ocupada', null=True)),
                ('disponivel', models.IntegerField(blank=True, db_column='Disponivel', null=True)),
                ('em_manutencao', models.IntegerField(blank=True, db_column='Em_Manutencao', null=True)),
                ('salaid', models.ForeignKey(db_column='SalaID', on_delete=django.db.models.deletion.DO_NOTHING, to='main.sala')),
            ],
            options={
                'db_table': 'estado_sala',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, db_column='Nome', max_length=255, null=True)),
                ('codigo_curso', models.IntegerField(db_column='Codigo_Curso')),
                ('ucid', models.ForeignKey(db_column='UCID', on_delete=django.db.models.deletion.DO_NOTHING, to='main.uc')),
            ],
            options={
                'db_table': 'curso',
            },
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('gambelas', models.IntegerField(blank=True, db_column='Gambelas', null=True)),
                ('penha', models.IntegerField(blank=True, db_column='Penha', null=True)),
                ('portimao', models.IntegerField(blank=True, db_column='Portimao', null=True)),
                ('salaid', models.ForeignKey(db_column='SalaID', on_delete=django.db.models.deletion.DO_NOTHING, to='main.sala')),
            ],
            options={
                'db_table': 'campus',
            },
        ),
        migrations.CreateModel(
            name='PedidoDeUc',
            fields=[
                ('pedidoid2', models.OneToOneField(db_column='PedidoID2', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.pedido')),
                ('ucid', models.ForeignKey(db_column='UCID', on_delete=django.db.models.deletion.DO_NOTHING, to='main.uc')),
            ],
            options={
                'db_table': 'pedido_de_uc',
            },
        ),
        migrations.CreateModel(
            name='PedidoDeHorario',
            fields=[
                ('pedidoid2', models.OneToOneField(db_column='PedidoID2', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.pedido')),
            ],
            options={
                'db_table': 'pedido_de_horario',
                'unique_together': {('pedidoid2',)},
            },
        ),
        migrations.CreateModel(
            name='Estadouc',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('ativada', models.IntegerField(blank=True, db_column='Ativada', null=True)),
                ('sem_curso', models.IntegerField(blank=True, db_column='Sem curso', null=True)),
                ('desativada', models.IntegerField(blank=True, db_column='Desativada', null=True)),
                ('sem_regente', models.IntegerField(blank=True, db_column='Sem regente', null=True)),
                ('ucid', models.ForeignKey(db_column='UCID', on_delete=django.db.models.deletion.DO_NOTHING, to='main.uc')),
            ],
            options={
                'db_table': 'estadouc',
                'unique_together': {('id', 'ucid')},
            },
        ),
        migrations.CreateModel(
            name='PedidoDeSala',
            fields=[
                ('pedidoid2', models.OneToOneField(db_column='PedidoID2', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.pedido')),
                ('salaid', models.ForeignKey(db_column='SalaID', on_delete=django.db.models.deletion.DO_NOTHING, to='main.sala')),
            ],
            options={
                'db_table': 'pedido_de_sala',
                'unique_together': {('pedidoid2', 'salaid')},
            },
        ),
        migrations.CreateModel(
            name='DocenteUc',
            fields=[
                ('docentepessoaid', models.OneToOneField(db_column='DocentePessoaID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.docente')),
                ('ucid', models.ForeignKey(db_column='UCID', on_delete=django.db.models.deletion.DO_NOTHING, to='main.uc')),
            ],
            options={
                'db_table': 'docente_uc',
                'unique_together': {('docentepessoaid', 'ucid')},
            },
        ),
    ]
