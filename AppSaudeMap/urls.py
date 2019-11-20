from django.urls import path
from AppSaudeMap.views import Index, CadastroIndividual, ListaFichaIndividual,\
    AtualizaFichaIndividual, MapaFichaIndividual, DeletaFichaIndividual
from SaudeMap.models import FichaDoenca

urlpatterns = [
    path('',Index.as_view(), name="index"),
    path('saudemap/', ListaFichaIndividual.as_view(), name='lista_cadastro_individual'),
    path('saudemap/cadastroIndividual', CadastroIndividual.as_view(model=FichaDoenca), name="cadastro_individual"),
    path('saudemap/<pk>', AtualizaFichaIndividual.as_view(model=FichaDoenca), name="atualiza_cadastro_individual"),
    path('saudemap/saudemap/mapa', MapaFichaIndividual.as_view(model=FichaDoenca), name='mapa_cadastro_individual'),
    path('saudemap/excluir/<pk>', DeletaFichaIndividual.as_view(model=FichaDoenca), name="deleta_cadastro_individual"),
]
