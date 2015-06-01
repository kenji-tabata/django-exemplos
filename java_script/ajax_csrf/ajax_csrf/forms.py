from django import forms
from ajax_csrf.models import Usuario
from ajax_csrf.models import Comentario

class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ('nome','email')
        
class ComentarioForm(forms.ModelForm):
    
    class Meta:
        model = Comentario
        fields = '__all__'