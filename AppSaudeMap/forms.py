from django import forms
from SaudeMap.models import FichaDoenca

class CriaForm(forms.ModelForm):
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=FichaDoenca.OPCOES)
    class Meta:
        model = FichaDoenca
        fields = ['cnsProfissional', 'cbo','cnes','ine','data','cnsCidadao','cnsResponsavelFamiliar','microArea','nomeCompleto','nomeSocial','dataNascimento','sexo']
        attrs = {'class':'form-control'}
        widgets = {
            'sexo':forms.RadioSelect(choices=FichaDoenca.OPCOES,attrs=attrs)
        }