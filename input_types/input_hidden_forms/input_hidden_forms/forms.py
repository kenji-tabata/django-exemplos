from django import forms
from input_hidden_forms.models import Hidden

class HiddenForm(forms.ModelForm):
    dado = forms.CharField(widget=forms.HiddenInput(), initial='input hidden')
    class Meta:
        model = Hidden
        fields = ('nome', 'dado')