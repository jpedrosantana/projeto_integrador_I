# Generated by Django 3.2 on 2021-11-10 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_empreendimento_nome_usuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ('nome',)},
        ),
        migrations.AlterModelOptions(
            name='condicao_pagamento',
            options={'ordering': ('nome',)},
        ),
    ]
