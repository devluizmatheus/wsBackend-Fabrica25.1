# Generated by Django 5.1.6 on 2025-03-02 00:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='conteudo_principal',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='abstract',
            new_name='resumo',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='section',
            new_name='secao',
        ),
        migrations.RemoveField(
            model_name='article',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
        migrations.AddField(
            model_name='article',
            name='data_publicacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='article',
            name='titulo',
            field=models.CharField(default=1, max_length=255, verbose_name='Titulo'),
            preserve_default=False,
        ),
    ]
