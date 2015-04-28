from django import forms
from checkbox_forms.models import CheckBox

class CheckboxForm(forms.ModelForm):
    assinar = forms.ChoiceField(
        label='Desejo receber os e-mails', 
        initial='Desejo receber os e-mails', 
        widget=forms.CheckboxInput,
    )
    
    class Meta:
        model = CheckBox
        fields = ('email','assinar',)