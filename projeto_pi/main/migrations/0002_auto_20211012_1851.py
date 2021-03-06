# Generated by Django 3.2 on 2021-10-12 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empreendimento',
            name='facebook',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='empreendimento',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='imagens'),
        ),
        migrations.AlterField(
            model_name='empreendimento',
            name='instagram',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='empreendimento',
            name='nome_empreendimento',
            field=models.CharField(max_length=50),
        ),
    ]
