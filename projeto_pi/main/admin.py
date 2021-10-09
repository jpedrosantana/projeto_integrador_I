from django.contrib import admin
from .models import Empreendimento

# Register your models here.
@admin.register(Empreendimento)
class EmpreendimentoAdmin(admin.ModelAdmin):
    list_display = ['cadastro',
                    'nome_empreendedor', 
                    'nome_empreendimento', 
                    'telefone',  
                    'instagram',  
                    'facebook',] #Campos visíveis na tela

    list_filter = ['nome_empreendimento', 'instagram', 'facebook'] #Campos que são usados como filtro de dados

    #prepopulated_fields =  #Campos preenchidos automaticamente

"""
   list_editable=['nome_empreendedor', 
                    'nome_empreendimento', 
                    'telefone',  
                    'instagram',  
                    'facebook', 
                    'descricao', 
                    'imagem'] #Campos que podem ser editados
"""