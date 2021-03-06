from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
# Criação da(s) tabela(s)
class Condicao_Pagamento(models.Model):
    nome = models.CharField(max_length=30)

    class Meta:
        ordering=('nome',)

    def __str__(self):
        """String representing the object"""
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    class Meta:
        ordering=('nome',)

    def __str__(self):
        """String representing the object"""
        return self.nome

    def get_absolute_url(self):
        return reverse('main:listar_empreendimento_categoria', args=[self.nome])
        
class Empreendimento(models.Model):
    cadastro = models.AutoField(primary_key=True)
    nome_empreendedor = models.CharField(max_length=20)
    nome_empreendimento = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11, blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    descricao = models.TextField(max_length=200)
    imagem = models.ImageField(upload_to='imagens')
    imagem2 = models.ImageField(upload_to='imagens', blank=True)
    imagem3 = models.ImageField(upload_to='imagens', blank=True)
    nome_usuario = models.ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)
    condicao_pagamento = models.ManyToManyField(Condicao_Pagamento)
    categoria = models.ManyToManyField(Categoria)

    class Meta:
        ordering=('nome_empreendimento',) #faz o ordenamento por empreendimento

    def __str__(self):
        return self.nome_empreendimento

    def get_absolute_url(self):
        return reverse('main:detalhes_empreendimento', args=[self.cadastro])

