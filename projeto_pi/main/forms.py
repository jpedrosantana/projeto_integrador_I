from django import forms
from .models import Empreendimento

class EmpreendimentoForm(forms.ModelForm):
    class Meta:
        model = Empreendimento
        fields = ('nome_empreendedor', 'nome_empreendimento', 'telefone', 'instagram', 'facebook', 'descricao', 'imagem')
