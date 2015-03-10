from django import forms
from d14_django_forms_textbox.models import TextBox

class TextboxForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = TextBox
        fields = ('nome', 'email','url','data','valor','numero','mensagem','senha')