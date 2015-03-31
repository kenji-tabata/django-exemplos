from django import forms
from f16_auto_validar_forms.models import Formulario

class FormularioForm(forms.ModelForm):
    
    class Meta:
        model = Formulario
        fields = ('nome','cpf','preenchido','nasc','sexo','email','ddd','telefone','end','bairro','cidade','estado','cep',
        'resp',)