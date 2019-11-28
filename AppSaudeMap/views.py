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
    
#http://prettyprinted.com/l/Log
#https://pt.stackoverflow.com/questions/236017/exportando-dados-em-json-ou-txt-no-python    
'''
def escrever_json(lista):
    with open('meu_arquivo.json', 'w') as f:
        json.dump(lista, f)

def carregar_json(arquivo):
    with open('meu_arquivo.json', 'r') as f:
        return json.load(f)

minha_lista = ['João', 'Maria', 'José']
escrever_json(minha_lista)

'''
#https://stackoverflow.com/questions/2428092/creating-a-json-response-using-django-and-python
#https://pypi.org/project/django-json-field/    
    