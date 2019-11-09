from django.urls import path
from AppSaudeMap.views import Index, CadastroIndividual
from SaudeMap.models import FichaDoenca

urlpatterns = [
    path('',Index.as_view(), name="index"),
    path('saudemap/cadastroIndividual', CadastroIndividual.as_view(model=FichaDoenca), name="cadastro_individual"),
]
