from django import forms
from d20_django_forms_input_hidden.models import Hidden

class HiddenForm(forms.ModelForm):
    dado = forms.CharField(widget=forms.MultipleHiddenInput(), initial='input hidden')
    class Meta:
        model = Hidden
        fields = ('nome', 'dado')