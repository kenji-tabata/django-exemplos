from django import forms
from d23_django_forms_auto_validar.models import Formulario

class FormularioForm(forms.ModelForm):
    
    class Meta:
        model = Formulario
        fields = ('nome','cpf','preenchido','nasc','sexo','email','ddd','telefone','end','bairro','cidade','estado','cep',
        'resp',)