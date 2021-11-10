from django import forms
from .models import Empreendimento
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmpreendimentoForm(forms.ModelForm):
    class Meta:
        model = Empreendimento
        fields = ('nome_empreendedor', 'nome_empreendimento', 'telefone', 'instagram', 'facebook', 'descricao', 'imagem')

#Formulario para registro de usuário
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True) #campo personalizado, por padrão é preciso apenas do username e password

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user