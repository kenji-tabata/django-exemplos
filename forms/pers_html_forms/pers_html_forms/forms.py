from django import forms
from pers_html_forms.models import Formulario

class FormularioForm(forms.ModelForm):
    # Definições do Radio Button
    SEXO_LIST = (
        ('masc', 'Masculino'),
        ('fem', 'Feminino'),
    )
    
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=SEXO_LIST, initial='masc' )
    
    # Definições do Combobox
    ESTADOS_LIST = (
        ('', 'Escolha o Estado'),
        ('SC', 'Santa Catarina'),
        ('MG', 'Minas Gerais'),
        ('RJ', 'Rio de Janeiro'),
        ('SP', 'São Paulo'),
    )
    
    estado = forms.ChoiceField(ESTADOS_LIST, initial='Escolha o Estado')
    
    # Definições do Checkbox Multi
    CHECKBOX_LIST = (
        ('i1', 'Item 01'),
        ('i2', 'Item 02'),
        ('i3', 'Item 03'),
        ('i4', 'Item 04'),
        ('i5', 'Item 05'),
        ('i6', 'Item 06'),
    )
    resp = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CHECKBOX_LIST )
    
    # Defições do Formulário
    class Meta:
        model = Formulario
        fields = '__all__'
    
    
    
    