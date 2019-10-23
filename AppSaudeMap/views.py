from django.views.generic import TemplateView
from SaudeMap.models import FichaDoenca

class Index(TemplateView):
    template_name = "index.html"