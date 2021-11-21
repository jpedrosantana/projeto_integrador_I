from django import forms
from .models import Condicao_Pagamento, Categoria, Empreendimento
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
class EmpreendimentoForm(forms.ModelForm):

	numeric = RegexValidator(r'^[0-9]*$', 'Utilize somente números')

	pagamentos = forms.ModelMultipleChoiceField(queryset=Condicao_Pagamento.objects.all(), widget=forms.CheckboxSelectMultiple, required=True)	
	categorias = forms.ModelMultipleChoiceField(queryset=Categoria.objects.all(), widget=forms.CheckboxSelectMultiple, required=True)

	telefone = forms.CharField(max_length=11, validators=[numeric])
	
	class Meta:
		model = Empreendimento
		fields = ('nome_empreendedor', 'nome_empreendimento', 'telefone', 'instagram', 'facebook', 'descricao',
		 'imagem', 'imagem2', 'imagem3', 'pagamentos', 'categorias')

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