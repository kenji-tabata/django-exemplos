from django import forms
from local_flavor_form_validacao.models import Cliente
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