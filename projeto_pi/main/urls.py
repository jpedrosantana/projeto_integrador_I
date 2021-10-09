from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'main'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('empreendimentos/', views.listar_empreendimentos, name='listar_empreendimentos'),
    path('empreendimento/<int:cadastro>', views.detalhes_empreendimento, name='detalhes_empreendimento')
]