from django import forms
from d19_django_forms_select_multi.models import Select

class SelectForm(forms.ModelForm):
    
    tipo = forms.ChoiceField(widget=forms.HiddenInput )
    
    class Meta:
        model = Select
        fields = ('tipo',)