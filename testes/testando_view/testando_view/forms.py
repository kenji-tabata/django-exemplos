from django import forms
from testando_view.models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ('nome','email','data','mensagem',)
        