from django import forms
from testando_template.models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'
        