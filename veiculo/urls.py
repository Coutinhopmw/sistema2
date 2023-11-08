from django.urls import path

from veiculo.views import FotoVeiculo, ListarVeiculos, APIListarCriarVeiculos, APIObterEditarDeletarVeiculos

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='veiculos'),
    path('api/', APIListarCriarVeiculos.as_view(), name='api-listar-criar-veiculos'),
    path('api/<int:pk>/', APIObterEditarDeletarVeiculos.as_view(), name='api-obter-editar-deletar-veiculos'),
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='foto-veiculo')
]