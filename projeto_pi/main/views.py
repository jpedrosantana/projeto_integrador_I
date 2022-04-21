from django import http
from django.shortcuts import render, get_object_or_404, redirect

from .forms import EmpreendimentoForm, NewUserForm
from .models import Empreendimento,  Categoria, Condicao_Pagamento
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def listar_empreendimentos(request, categoria=None):
    lista_empreendimentos = Empreendimento.objects.all()
    lista_categorias = Categoria.objects.all()

    #https://about-wendrew.medium.com/realizando-buscas-em-registros-com-django-936dfe1215bb
    busca = request.GET.get("search") #Pega a busca que veio do input

    if busca:
        #filtra o nome do empreendimento por algo que contém na busca
        busca_empreendimento = Empreendimento.objects.filter(nome_empreendimento__icontains = busca) 
        contexto = {'lista_empreendimentos': busca_empreendimento,
                    'lista_categorias': lista_categorias,
                    'categoria': categoria,}
        #Renderiza apenas com o que está na busca
        return render(request, 'empreendimentos/listar.html', contexto)

    if categoria:
        categoria = get_object_or_404(Categoria, nome=categoria)
        lista_empreendimentos = Empreendimento.objects.filter(categoria=categoria)
    

    contexto = {'lista_empreendimentos': lista_empreendimentos,
                'lista_categorias': lista_categorias,
                'categoria': categoria,
                }
    return render(request, 'empreendimentos/listar.html', contexto)

def detalhes_empreendimento(request, cadastro):
    empreendimento = get_object_or_404(Empreendimento, cadastro=cadastro)
    contexto = {'empreendimento': empreendimento,}
    return render(request, 'empreendimentos/detalhes.html', contexto)

def anuncie(request):
    # if this is a POST request we need to process the form data
    form = EmpreendimentoForm()

    if request.method == 'POST':
        #print(request.POST)
        # create a form instance and populate it with data from the request:
        form = EmpreendimentoForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Anúncio incluído com sucesso!' )

            return http.HttpResponseRedirect('/empreendimentos')
            
    contexto = {'form': form}

    return render(request, 'anuncie.html', contexto)

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

