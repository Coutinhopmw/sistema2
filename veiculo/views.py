from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse, Http404
from django.views.generic import ListView

from sistema2.bibliotecas import LoginObrigatorio
from veiculo.models import Veiculo


class ListarVeiculos(LoginObrigatorio, ListView):
    """
        view para listar veiculos cadastrados
    """

    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

class FotoVeiculo(LoginObrigatorio):
    """
        view para retornar a foto dos veiculos
    """
    def get(self,request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto não existe ou acesso não altorizado")
        except Exception as exception:
            raise Exception
