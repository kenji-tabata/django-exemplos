Local Flavor
===

[https://docs.djangoproject.com/en/1.8/topics/localflavor/](https://docs.djangoproject.com/en/1.8/topics/localflavor/)

Módulo do Django que contem componentes adicionais como combobox dos estados brasileiros e validações dos campos do 
Django Forms de cada país.

Para instalar utilize...

    pip install django-localflavor


Combobox dos estados brasileiros
---

```python
# mysite/polls/forms.py
from django import forms
from exemplo.models import Combobox
from localflavor.br.br_states import STATE_CHOICES

class ComboboxForm(forms.ModelForm):
    estado = forms.ChoiceField(choices=STATE_CHOICES)
    class Meta:
        model = Combobox
        fields = ('estado',)
```


Validações do Django Forms
---

```python
# mysite/polls/forms.py
from django import forms
from exemplo.models import Cliente
from localflavor.br.forms import BRZipCodeField
from localflavor.br.forms import BRPhoneNumberField
from localflavor.br.forms import BRCPFField
from localflavor.br.forms import BRCNPJField
from localflavor.br.forms import BRStateChoiceField

class ClienteForm(forms.ModelForm):
    
    cep = BRZipCodeField()
    tel = BRPhoneNumberField()
    cpf = BRCPFField()
    cnpj =BRCNPJField()
    estados = BRStateChoiceField()
    
    class Meta:
        model = Cliente
```