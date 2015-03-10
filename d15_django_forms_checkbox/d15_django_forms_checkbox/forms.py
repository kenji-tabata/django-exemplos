from django import forms
from d15_django_forms_checkbox.models import CheckBox

class CheckboxForm(forms.ModelForm):
    assinar = forms.ChoiceField(widget=forms.CheckboxInput )
    
    class Meta:
        model = CheckBox
        fields = ('email','assinar',)