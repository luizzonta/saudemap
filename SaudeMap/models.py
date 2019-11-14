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

    OPCOES_RESPONSAVEL_FAMILIAR = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    responsavelFamiliar = models.CharField(max_length=3, choices=OPCOES_RESPONSAVEL_FAMILIAR, blank=True, null=True)

    cnsResponsavelFamiliar = models.CharField(
        max_length=10,
        null=True,
        blank=False
    )
    microArea = models.CharField(
        max_length=2,
        null=True,
        blank=False
    )

    nomeCompleto = models.CharField(
        max_length=255,
        null=True,
        blank=False
    )
    nomeSocial = models.CharField(
        max_length=255,
        null=True,
        blank=False
    )
    
    dataNascimento = models.DateField(
        max_length=10,
        null=True,
        blank=False
    )    
         
    OPCOES_SEXO = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    )
    sexo = models.CharField(max_length=10, choices=OPCOES_SEXO, blank=True, null=True)

    OPCOES_RACA_COR = (
        ('Branca', 'Branca'),
        ('Preta', 'Preta'),
        ('Parda', 'Parda'),
        ('Amarela', 'Amarela'),
        ('Indígena', 'Indígena'),
    )
    racaCor = models.CharField(max_length=10, choices=OPCOES_RACA_COR, blank=True, null=True)

    telefoneCelular = models.BigIntegerField(
        null=True,
        blank=False
    )
    email = models.CharField(
        max_length=255,
        null=True,
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

    OPCOES_PESO = (
        ('Abaixo do peso', 'Abaixo do peso'),
        ('Peso adequado', 'Peso adequado'),
        ('Acima do peso', 'Acima do peso'),
    )
    peso = models.CharField(max_length=20, choices=OPCOES_PESO, blank=True, null=True)

    OPCOES_GESTANTE = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    gestante = models.CharField(max_length=3, choices=OPCOES_GESTANTE, blank=True, null=True)

    OPCOES_FUMANTE = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    fumante = models.CharField(max_length=3, choices=OPCOES_FUMANTE, blank=True, null=True)

    OPCOES_DOENCA_RESPIRATORIA = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    doencaRespiratoria  = models.CharField(max_length=3, choices=OPCOES_DOENCA_RESPIRATORIA, blank=True, null=True)

    OPCOES_USA_ALCOOL = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    usaAlcool = models.CharField(max_length=3, choices=OPCOES_USA_ALCOOL, blank=True, null=True)

    OPCOES_USA_DROGAS = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    usaDrogas = models.CharField(max_length=3, choices=OPCOES_USA_DROGAS, blank=True, null=True)

    OPCOES_HIPERTENSAO_ARTERIAL = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    hipertensaoArterial = models.CharField(max_length=3, choices=OPCOES_HIPERTENSAO_ARTERIAL, blank=True, null=True)

    OPCOES_DIABETES = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    diabetes = models.CharField(max_length=3, choices=OPCOES_DIABETES, blank=True, null=True)

    OPCOES_AVC_DERRAME = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    avcDerrame = models.CharField(max_length=3, choices=OPCOES_AVC_DERRAME, blank=True, null=True)

    OPCOES_INFARTO = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    infarto = models.CharField(max_length=3, choices=OPCOES_INFARTO, blank=True, null=True)

    OPCOES_DOENCA_CARDIACA = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    doencaCardiaca = models.CharField(max_length=3, choices=OPCOES_DOENCA_CARDIACA, blank=True, null=True)

    OPCOES_PROBLEMA_RINS = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    problemaRins = models.CharField(max_length=3, choices=OPCOES_PROBLEMA_RINS, blank=True, null=True)

    OPCOES_HENSANIASE = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    hensaniase = models.CharField(max_length=3, choices=OPCOES_HENSANIASE, blank=True, null=True)

    OPCOES_TUBERCULOSE = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    tuberculose = models.CharField(max_length=3, choices=OPCOES_TUBERCULOSE, blank=True, null=True)

    OPCOES_CANCER = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    cancer = models.CharField(max_length=3, choices=OPCOES_CANCER, blank=True, null=True)

    OPCOES_SAUDEMENTAL = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    saudeMental = models.CharField(max_length=3, choices=OPCOES_SAUDEMENTAL, blank=True, null=True)

    OPCOES_INTERNACAO = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    internacao = models.CharField(max_length=3, choices=OPCOES_INTERNACAO, blank=True, null=True)

    OPCOES_ACAMADO = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    acamado = models.CharField(max_length=3, choices=OPCOES_ACAMADO, blank=True, null=True)
    
    OPCOES_DOMICILIADO = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    domiciliado = models.CharField(max_length=3, choices=OPCOES_DOMICILIADO, blank=True, null=True)
    
    OPCOES_PLANTAS_MEDICINAIS = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    plantasMedicinais = models.CharField(max_length=3, choices=OPCOES_PLANTAS_MEDICINAIS, blank=True, null=True)

    latitude = models.CharField(
        max_length=255,
        null=True,
        blank=False
    )    
    longitude = models.CharField(
        max_length=255,
        null=True,
        blank=False
    )    

    objetos = models.Manager()