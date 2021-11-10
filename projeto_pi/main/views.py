from django.shortcuts import render, get_object_or_404, redirect

from .forms import EmpreendimentoForm, NewUserForm
from .models import Empreendimento
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def listar_empreendimentos(request):
    lista_empreendimentos = Empreendimento.objects.all()
    contexto = {'lista_empreendimentos': lista_empreendimentos}
    return render(request, 'empreendimentos/listar.html', contexto)

def detalhes_empreendimento(request, cadastro):
    empreendimento = get_object_or_404(Empreendimento, cadastro=cadastro)
    contexto = {'empreendimento': empreendimento,}
    return render(request, 'empreendimentos/detalhes.html', contexto)

def anuncie(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmpreendimentoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmpreendimentoForm()

    return render(request, 'anuncie.html', {'form': form})

#view para o cadastro de usuário
def register_request(request):
	if request.method == "POST": #Valida se o método é post
		form = NewUserForm(request.POST)
		if form.is_valid():
            #salva o usuário e faz login com ele
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})