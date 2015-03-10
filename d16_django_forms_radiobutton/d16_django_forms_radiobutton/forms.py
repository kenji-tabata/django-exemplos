from django import forms
from d16_django_forms_radiobutton.models import Radio

class RadioForm(forms.ModelForm):
    RADIO_LIST = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),
    )
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=RADIO_LIST )
    
    class Meta:
        model = Radio
        fields = ('sexo',)