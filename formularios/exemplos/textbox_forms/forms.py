from django import forms
from textbox_forms.models import Postagem

class PostagensForm(forms.ModelForm):
    
    class Meta:
        model = Postagem
        fields = ('titulo', 'email','url','rating','like','conteudo')