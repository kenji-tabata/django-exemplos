from django import forms
from pers_validar_forms.models import Formulario
from pers_validar_forms.validar import Validar

class FormularioForm(forms.ModelForm):
    # Defições do Formulário
    class Meta:
        model = Formulario
        fields = '__all__'
    
    
    # Validações do formulário
        
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) <= 4 :
            raise forms.ValidationError('O nome deve conter acima de 4 caracteres.')
        
        return nome
    
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        
        cpf = Validar.returnNumero(cpf)
        
        if Validar.verificaCPF(cpf):
            raise forms.ValidationError('O CPF deve conter no mínimo 11 digitos.')
            
        if Validar.numeroRepetidos(cpf) >= 8:
            raise forms.ValidationError('O CPF não pode conter apenas número repetidos')
        
        return cpf
            
    def clean_ddd(self):
        ddd = self.cleaned_data['ddd']
        
        if not Validar.verificarDdd(ddd):
            raise forms.ValidationError('O número do DDD está fora do padrão 00')
        
        return ddd
    
    def clean_telefone(self):
        tel = self.cleaned_data['telefone']
        
        if not Validar.verificarTelefone(tel):
            raise forms.ValidationError('O número de telefone está fora do padrão 0000-0000 ou 00000-00000')
        
        return tel
        
    def clean_cep(self):
        cep = self.cleaned_data['cep']
        
        if not Validar.verificarCep(cep):
            raise forms.ValidationError('O número de CEP está fora do padrão 00000-000')
        
        return cep