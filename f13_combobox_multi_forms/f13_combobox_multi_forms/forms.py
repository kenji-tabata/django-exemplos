from django import forms
from f13_combobox_multi_forms.models import Select

class SelectForm(forms.ModelForm):
    SELECT_LIST = (
        ('i1', 'Item 01'),
        ('i2', 'Item 02'),
        ('i3', 'Item 03'),
        ('i4', 'Item 04'),
        ('i5', 'Item 05'),
        ('i6', 'Item 06'),
        
    )
    tipo = forms.ChoiceField(widget=forms.SelectMultiple, choices=SELECT_LIST )
    
    class Meta:
        model = Select
        fields = ('tipo',)