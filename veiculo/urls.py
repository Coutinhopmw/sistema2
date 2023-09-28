from django.urls import path

from veiculo.views import FotoVeiculo, ListarVeiculos

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='veiculos'),
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='foto-veiculo')
]