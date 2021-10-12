from django.shortcuts import render, get_object_or_404
from .models import Empreendimento
from django.views.generic.edit import FormView

# Create your views here.

def listar_empreendimentos(request):
    lista_empreendimentos = Empreendimento.objects.all()
    contexto = {'lista_empreendimentos': lista_empreendimentos}
    return render(request, 'empreendimentos/listar.html', contexto)

def detalhes_empreendimento(request, cadastro):
    empreendimento = get_object_or_404(Empreendimento, cadastro=cadastro)
    contexto = {'empreendimento': empreendimento,}
    return render(request, 'empreendimentos/detalhes.html', contexto)