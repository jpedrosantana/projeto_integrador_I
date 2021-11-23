from django import forms
from .models import Condicao_Pagamento, Categoria, Empreendimento
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class EmpreendimentoForm(forms.ModelForm):
	class Meta:
		model = Empreendimento
		fields = ['nome_empreendedor', 'nome_empreendimento', 'telefone', 'instagram', 'facebook', 'descricao',
		 'imagem', 'imagem2', 'imagem3', 'condicao_pagamento', 'categoria']
		labels = {
        	'nome_empreendedor': 'Nome',
			'nome_empreendimento': 'Nome do produto/serviço',
			'imagem': 'Imagem principal',
        }
		widgets = {
            'nome_empreendedor': forms.TextInput(attrs={'placeholder': 'Seu nome', 'size': 40}),
			'nome_empreendimento': forms.TextInput(attrs={'placeholder': 'Nome do produto ou serviço', 'size': 40}),
			'instagram': forms.TextInput(attrs={'placeholder': 'Ex: @exemplo', 'size': 40}),
			'facebook': forms.TextInput(attrs={'placeholder': 'Ex: facebook.com/exemplo', 'size': 40}),
			'descricao': forms.Textarea(attrs={'placeholder': 'Coloque as informações sobre o seu produto ou serviço', 'size': 40}),
        }

	numeric = RegexValidator(r'^[0-9]*$', 'Utilize somente números')

	condicao_pagamento = forms.ModelMultipleChoiceField(queryset=Condicao_Pagamento.objects.all(), widget=forms.CheckboxSelectMultiple, required=True, label='Pagamento')	

	categoria = forms.ModelMultipleChoiceField(queryset=Categoria.objects.all(), widget=forms.CheckboxSelectMultiple, required=True, label='Categorias')

	telefone = forms.CharField(max_length=11, validators=[numeric], widget=forms.TextInput(attrs={'size':40, 'placeholder': '1199998888'}))
	

#Formulario para registro de usuário
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'size': 40})) #campo personalizado, por padrão é preciso apenas do username e password

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		widgets = {
			'username': forms.TextInput(attrs={'size': 40}),
		}

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user