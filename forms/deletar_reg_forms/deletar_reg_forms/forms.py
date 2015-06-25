from django import forms
from deletar_reg_forms.models import Formulario

class FormularioForm(forms.ModelForm):
    
    class Meta:
        model = Formulario
        fields = '__all__'