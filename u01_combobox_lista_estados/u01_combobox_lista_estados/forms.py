from django import forms
from u01_combobox_lista_estados.models import Combobox
from localflavor.br.br_states import STATE_CHOICES

class ComboboxForm(forms.ModelForm):
    estado = forms.ChoiceField(choices=STATE_CHOICES)
    class Meta:
        model = Combobox
        fields = ('estado',)