# Generated by Django 4.1 on 2022-08-27 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_alter_cliente_cpf_alter_vendedor_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicos',
            name='Status',
            field=models.CharField(choices=[('I', 'iniciado'), ('F', 'Finalizado'), ('N_I', 'Não iniciado'), ('C_P', 'Com problema')], max_length=4),
        ),
    ]
