from django.db import models
from django.urls import reverse

# Create your models here.
# Criação da(s) tabela(s)
class Empreendimento(models.Model):
    cadastro = models.AutoField(primary_key=True)
    nome_empreendedor = models.CharField(max_length=20)
    nome_empreendimento = models.CharField(max_length=30)
    telefone = models.CharField(max_length=11, blank=True)
    instagram = models.CharField(max_length=30, blank=True)
    facebook = models.CharField(max_length=30, blank=True)
    descricao = models.TextField(max_length=200)
    imagem = models.ImageField(upload_to='imagens')

    class Meta:
        ordering=('nome_empreendimento',) #faz o ordenamento por empreendimento

    def __str__(self):
        return self.nome_empreendimento

    def get_absolute_url(self):
        return reverse('main:detalhes_empreendimento', args=[self.cadastro])
