from django.views.generic import TemplateView
from SaudeMap.models import FichaDoenca
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

class Index(TemplateView):
    template_name = "index.html"

class ListaFichaIndividual(ListView):
    template_name = "listaFichaIndividual.html"
    model = FichaDoenca
    context_object_name = 'FichaDoenca'

class CadastroIndividual(CreateView):
    template_name = "cadastroIndividual.html"
    model = FichaDoenca()
    fields = '__all__'
    success_url = reverse_lazy("lista_cadastro_individual")
    
class AtualizaFichaIndividual(UpdateView):
    template_name = "atualizaCadastroIndividual.html"
    model = FichaDoenca()
    fields = '__all__'
    context_object_name = 'FichaDoenca'
    success_url = reverse_lazy("lista_cadastro_individual")

class MapaFichaIndividual(ListView):
    template_name = "mapaFichaIndividual.html"
    model = FichaDoenca
    context_object_name = 'FichaDoenca'
        