from django.views.generic import TemplateView
from SaudeMap.models import FichaDoenca
from django.contrib.messages.api import success
from audioop import reverse
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView

class Index(TemplateView):
    template_name = "index.html"

class CadastroIndividual(CreateView):
    template_name = "cadastroIndividual.html"
    model = FichaDoenca()
    fields = '__all__'
    success_url = reverse_lazy("index")    