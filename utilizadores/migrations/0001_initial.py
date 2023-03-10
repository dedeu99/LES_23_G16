# Generated by Django 4.1.7 on 2023-03-07 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            name='Docente',
            fields=[
                ('pessoaid', models.OneToOneField(db_column='PessoaID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='utilizadores.pessoa')),
            ],
            options={
                'db_table': 'docente',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoaid', models.ForeignKey(db_column='PessoaID', on_delete=django.db.models.deletion.DO_NOTHING, to='utilizadores.pessoa')),
            ],
            options={
                'db_table': 'funcionario',
            },
        ),
    ]
