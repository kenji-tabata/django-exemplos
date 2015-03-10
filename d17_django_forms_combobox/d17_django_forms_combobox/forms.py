from django import forms
from d17_django_forms_combobox.models import Combobox

class ComboboxForm(forms.ModelForm):
    COMBOBOX_LIST = (
        ('Grupo 01', (
                ('i1', 'Item 01'),
                ('i2', 'Item 02'),
                ('i3', 'Item 03'),
            )
        ),
        ('Grupo 02', (
                ('i4', 'Item 04'),
                ('i5', 'Item 05'),
                ('i6', 'Item 06'),
            )
        ),
        ('i7', 'Item 07'),
        ('i8', 'Item 08'),
        ('i9', 'Item 09'),
    )
    tipo = forms.ChoiceField(COMBOBOX_LIST)
    class Meta:
        model = Combobox
        fields = ('tipo',)