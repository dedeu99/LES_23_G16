# Generated by Django 4.1.5 on 2023-05-04 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoPedidos', '0002_funcionario_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnoLetivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_column='Nome', max_length=255)),
                ('data_inicial', models.DateField(db_column='DataInicial')),
                ('data_final', models.DateField(db_column='DataFinal')),
            ],
            options={
                'db_table': 'ano_letivo',
                'managed': True,
            },
        ),
    ]
