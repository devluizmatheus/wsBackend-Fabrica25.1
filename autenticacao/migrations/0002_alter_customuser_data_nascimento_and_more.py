# Generated by Django 5.1.6 on 2025-03-01 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True, verbose_name='Data Nascimento'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='numero_telefone',
            field=models.CharField(blank=True, max_length=50, verbose_name='Número de Telefone'),
        ),
    ]
