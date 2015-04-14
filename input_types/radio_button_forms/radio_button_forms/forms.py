from django import forms
from radio_button_forms.models import Radio

class RadioForm(forms.ModelForm):
    RADIO_LIST = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),
    )
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=RADIO_LIST )
    
    class Meta:
        model = Radio
        fields = ('sexo',)