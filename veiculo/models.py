from datetime import datetime

from django.db import models

from veiculo.consts import OPCOES_COMBUSTIVEIS, OPCOES_CORES, OPCOES_MARCAS


def diretorio_imagens_veiculo(instance,filename):
    return 'veiculos/fotos/{0}/{1}'.format(instance.id, filename)

class Veiculo(models.Model):
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.SmallIntegerField(choices=OPCOES_CORES)
    foto = models.ImageField(blank=True, null=True, upload_to=diretorio_imagens_veiculo)
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEIS)

    @property
    def veiculo_novo(self):
        return self.ano == datetime.now().year

    def __str__(self):
        return '{0} - {1} ({2}/{3})'.format(
            self.marca,
            self.modelo,
            self.ano,
            self.get_cor_display()
        )
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            foto_salva = self.foto
            self.foto = None
            super(Veiculo, self).save(*args,**kwargs)
            self.foto = foto_salva
            kwargs.update(force_insert = False)
        super(Veiculo,self).save(*args,**kwargs)
    
    def anos_de_uso(self):
        return datetime.now().year - self.ano