# Generated by Django 3.2 on 2021-10-08 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empreendimento',
            fields=[
                ('cadastro', models.AutoField(primary_key=True, serialize=False)),
                ('nome_empreendedor', models.CharField(max_length=20)),
                ('nome_empreendimento', models.CharField(max_length=30)),
                ('telefone', models.CharField(blank=True, max_length=11)),
                ('instagram', models.CharField(blank=True, max_length=30)),
                ('facebook', models.CharField(blank=True, max_length=30)),
                ('descricao', models.TextField(max_length=200)),
                ('imagem', models.ImageField(upload_to='imagens')),
            ],
            options={
                'ordering': ('nome_empreendimento',),
            },
        ),
    ]
