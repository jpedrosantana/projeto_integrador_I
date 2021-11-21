from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls import include


app_name = 'main'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('empreendimentos/', views.listar_empreendimentos, name='listar_empreendimentos'),
    path('empreendimentos/<str:categoria>/', views.listar_empreendimentos, name='listar_empreendimento_categoria'),
    path('empreendimento/<int:cadastro>', views.detalhes_empreendimento, name='detalhes_empreendimento'),
    path('anuncie/', views.anuncie, name='anuncie'),
    path('register/', views.register_request, name='register'),
]