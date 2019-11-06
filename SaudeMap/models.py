from django.db import models

class FichaDoenca(models.Model):
    
    cnsProfissional = models.CharField(
        max_length=15,
        null=True,
        blank=False
    )
    cbo = models.CharField(
        max_length=6,
        null=True,
        blank=False
    )
    cnes = models.CharField(
        max_length=7,
        null=True,
        blank=False
    )
    ine = models.CharField(
        max_length=10,
        null=True,
        blank=False
    )
    data = models.DateField(
        max_length=10,
        null=True,
        blank=False
    )
    cnsCidadao = models.CharField(
        max_length=15,
        null=True,
        blank=False
    )



    objetos = models.Manager()