from django import forms
from f03_textbox_forms.models import TextBox

class TextboxForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = TextBox
        fields = ('nome', 'email','url','data','valor','numero','mensagem','senha')