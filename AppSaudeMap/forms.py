from django import forms
from SaudeMap.models import FichaDoenca

class CriaForm(forms.ModelForm):
    responsavelFamiliar = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_RESPONSAVEL_FAMILIAR)
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_SEXO)
    racaCor = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_RACA_COR)
    peso = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_PESO)
    gestante = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_GESTANTE)
    fumante = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_FUMANTE)
    doencaRespiratoria = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_DOENCA_RESPIRATORIA)
    usaAlcool = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_USA_ALCOOL)
    usaDrogas = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_USA_DROGAS)
    hipertensaoArterial = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_HIPERTENSAO_ARTERIAL)
    diabetes = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_DIABETES)
    avcDerrame = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_AVC_DERRAME)
    infarto = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_INFARTO)
    doencaCardiaca = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_DOENCA_CARDIACA)
    problemaRins = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_PROBLEMA_RINS)
    hensaniase = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_HENSANIASE)
    tuberculose = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_TUBERCULOSE)
    cancer = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_CANCER)
    saudeMental = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_SAUDEMENTAL)
    internacao = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_INTERNACAO)
    acamado = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_ACAMADO)
    domiciliado = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_DOMICILIADO)
    plantasMedicinais = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES_PLANTAS_MEDICINAIS)
    
    class Meta:
        model = FichaDoenca
        fields = ['cnsProfissional', 'cbo','cnes','ine','data','cnsCidadao','cnsResponsavelFamiliar',
                  'responsavelFamiliar','microArea','nomeCompleto','nomeSocial','dataNascimento','sexo',
                  'racaCor', 'peso', 'gestante', 'fumante', 'doencaRespiratoria', 'usaAlcool', 'usaDrogas',
                  'hipertensaoArterial', 'diabetes', 'avcDerrame', 'infarto', 'doencaCardiaca', 'problemaRins',
                  'hensaniase', 'tuberculose', 'cancer', 'saudeMental', 'internacao', 'acamado', 'domiciliado',
                  'plantasMedicinais' ]
        attrs = {'class':'form-control'}
        widgets = {
            'responsavelFamiliar':forms.RadioSelect(choices=FichaDoenca.OPCOES_RESPONSAVEL_FAMILIAR,attrs=attrs)
            }
        widgets = {
            'sexo':forms.RadioSelect(choices=FichaDoenca.OPCOES_SEXO,attrs=attrs)
            }
        widgets = {
            'racaCor':forms.RadioSelect(choices=FichaDoenca.OPCOES_RACA_COR,attrs=attrs)
            }
        widgets = {
            'peso':forms.RadioSelect(choices=FichaDoenca.OPCOES_PESO,attrs=attrs)
            }
        widgets = {
            'gestante':forms.RadioSelect(choices=FichaDoenca.OPCOES_GESTANTE,attrs=attrs)
            }                
        widgets = {
            'fumante':forms.RadioSelect(choices=FichaDoenca.OPCOES_FUMANTE,attrs=attrs)
            }
        widgets = {
            'doencaRespiratoria':forms.RadioSelect(choices=FichaDoenca.OPCOES_DOENCA_RESPIRATORIA,attrs=attrs)
            }        
        widgets = {
            'usaAlcool':forms.RadioSelect(choices=FichaDoenca.OPCOES_USA_ALCOOL,attrs=attrs)
            }
        widgets = {
            'usaDrogas':forms.RadioSelect(choices=FichaDoenca.OPCOES_USA_DROGAS,attrs=attrs)
            }
        widgets = {
            'hipertensaoArterial':forms.RadioSelect(choices=FichaDoenca.OPCOES_HIPERTENSAO_ARTERIAL,attrs=attrs)
            }
        widgets = {
            'diabetes':forms.RadioSelect(choices=FichaDoenca.OPCOES_DIABETES,attrs=attrs)
            }
        widgets = {
            'avcDerrame':forms.RadioSelect(choices=FichaDoenca.OPCOES_AVC_DERRAME,attrs=attrs)
            }
        widgets = {
            'infarto':forms.RadioSelect(choices=FichaDoenca.OPCOES_INFARTO,attrs=attrs)
            }
        widgets = {
            'doencaCardiaca':forms.RadioSelect(choices=FichaDoenca.OPCOES_DOENCA_CARDIACA,attrs=attrs)
            }
        widgets = {
            'problemaRins':forms.RadioSelect(choices=FichaDoenca.OPCOES_PROBLEMA_RINS,attrs=attrs)
            }
        widgets = {
            'hensaniase':forms.RadioSelect(choices=FichaDoenca.OPCOES_HENSANIASE,attrs=attrs)
            }
        widgets = {
            'tuberculose':forms.RadioSelect(choices=FichaDoenca.OPCOES_TUBERCULOSE,attrs=attrs)
            }
        widgets = {
            'cancer':forms.RadioSelect(choices=FichaDoenca.OPCOES_CANCER,attrs=attrs)
            }
        widgets = {
            'saudeMental':forms.RadioSelect(choices=FichaDoenca.OPCOES_SAUDEMENTAL,attrs=attrs)
            }
        widgets = {
            'internacao':forms.RadioSelect(choices=FichaDoenca.OPCOES_INTERNACAO,attrs=attrs)
            }
        widgets = {
            'acamado':forms.RadioSelect(choices=FichaDoenca.OPCOES_ACAMADO,attrs=attrs)
            }
        widgets = {
            'domiciliado':forms.RadioSelect(choices=FichaDoenca.OPCOES_DOMICILIADO,attrs=attrs)
            }
        widgets = {
            'plantasMedicinais':forms.RadioSelect(choices=FichaDoenca.OPCOES_PLANTAS_MEDICINAIS,attrs=attrs)
            }
        