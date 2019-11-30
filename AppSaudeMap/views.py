from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from SaudeMap.models import FichaDoenca
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
import json

class Index(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "index.html"

class ListaFichaIndividual(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = "listaFichaIndividual.html"
    model = FichaDoenca
    context_object_name = 'FichaDoenca'

class CadastroIndividual(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = "cadastroIndividual.html"
    model = FichaDoenca()
    fields = '__all__'
    success_url = reverse_lazy("lista_cadastro_individual")
    
class AtualizaFichaIndividual(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    template_name = "atualizaCadastroIndividual.html"
    model = FichaDoenca()
    fields = '__all__'
    context_object_name = 'FichaDoenca'
    success_url = reverse_lazy("lista_cadastro_individual")

class MapaFichaIndividual(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = "mapaFichaIndividual.html"
    model = FichaDoenca
    context_object_name = 'FichaDoenca'

class DeletaFichaIndividual(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = "excluiFichaIndividual.html"
    model = FichaDoenca()
    context_object_name = 'FichaDoenca'
    success_url = reverse_lazy("lista_cadastro_individual")        
    
class GraficoFichaIndividual(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = "graficoFichaIndividual.html"
    model = FichaDoenca
    context_object_name = 'FichaDoenca'
