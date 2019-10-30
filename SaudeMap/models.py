from django.db import models

class FichaDoenca(models.Model):
    
    cnsProfissional = models.CharField(
        max_length=15,
        null=False,
        blank=False
    )

    cbo = models.CharField(
        max_length=6,
        null=False,
        blank=False
    )
    cnes = models.CharField(
        max_length=7,
        null=False,
        blank=False
    )
    ine = models.CharField(
        max_length=10,
        null=False,
        blank=False
    )
    data = models.DateField(
        null=False,
        blank=False
    )
    cnsCidadao = models.CharField(
        max_length=15,
        null=False,
        blank=False
    )
    responsavelFamiliar = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    cnsresponsavelFamiliar = models.CharField(
        max_length=10,
        null=False,
        blank=False
    )
    microarea = models.CharField(
        max_length=2,
        null=False,
        blank=False
    )
    
    nomeCompleto = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    nomeSocial = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    dataNascimento = models.DateField(
        null=False,
        blank=False
    )
    sexo = models.CharField(
        max_length=1,
        null=False,
        blank=False
    )
    racaCor = models.CharField(
        max_length=10,
        null=False,
        blank=False
    )
    telefoneCelular = models.BigIntegerField(
        null=False,
        blank=False
    )
    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    endereco = models.CharField(
        max_length=255,
        null=True,
        blank=False
    )
    numero = models.CharField(
        max_length=10,
        null=True,
        blank=False
    )
    bairro = models.CharField(
        max_length=50,
        null=True,
        blank=False
    )
    cidade = models.CharField(
        max_length=50,
        null=True,
        blank=False
    )
    uf = models.CharField(
        max_length=2,
        null=True,
        blank=False
    )
    
    gestante = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    
    peso = models.CharField(  
        max_length=255,
        null=True,
        blank=False
    )
    
    fumante = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    usaAlcool = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    usaDrogas = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    hipertensaoArterial = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    diabetes = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    avcDerrame = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    infarto = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    doencaCardiaca = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    problemaRins = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    doencaRespiratoria = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    hensaniase = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    tuberculose = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    cancer = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    internacao = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    saudeMenta = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    acamado = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    domiciliado = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    plantasMedicinais = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    praticasIntegrativasComplementares = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    
    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=8,
        null=True,
        blank=False
    )    
    longetude = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        null=True,
        blank=False
    )    
    objetos = models.Manager()