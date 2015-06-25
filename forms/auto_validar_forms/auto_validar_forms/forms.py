from django import forms
from auto_validar_forms.models import Formulario

class FormularioForm(forms.ModelForm):
    
    class Meta:
        model = Formulario
        fields = '__all__'