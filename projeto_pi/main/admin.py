from django.contrib import admin
from .models import Condicao_Pagamento, Empreendimento, Categoria

# Register your models here.
@admin.register(Empreendimento)
class EmpreendimentoAdmin(admin.ModelAdmin):
    list_display = ['cadastro',
                    'nome_empreendedor', 
                    'nome_empreendimento', 
                    'telefone',  
                    'instagram',  
                    'facebook',
                    'descricao',
                    'imagem',
                    'imagem2',
                    'imagem3',
                    ] #Campos visíveis na tela,

    list_filter = ['nome_empreendimento', 'instagram', 'facebook'] #Campos que são usados como filtro de dados

    #prepopulated_fields =  #Campos preenchidos automaticamente

@admin.register(Condicao_Pagamento)
class Condicao_PagamentoAdmin(admin.ModelAdmin):
    model = Condicao_Pagamento
    
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria
