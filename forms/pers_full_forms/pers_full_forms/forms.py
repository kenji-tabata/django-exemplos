from django import forms
from pers_full_forms.models import Formulario

class FormularioForm(forms.ModelForm):
    # Definições do Radio Button
    SEXO_LIST = (
        ('masc', 'Masculino'),
        ('fem', 'Feminino'),
    )
    
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=SEXO_LIST, initial='masc' )
    
    # Definições do Combobox
    ESTADOS_LIST = (
        ('', 'Escolha o Estado'),
        ('SC', 'Santa Catarina'),
        ('MG', 'Minas Gerais'),
        ('RJ', 'Rio de Janeiro'),
        ('SP', 'São Paulo'),
    )
    
    estado = forms.ChoiceField(ESTADOS_LIST, initial='Escolha o Estado')
    
    # Definições do Checkbox Multi
    CHECKBOX_LIST = (
        ('i1', 'Item 01'),
        ('i2', 'Item 02'),
        ('i3', 'Item 03'),
        ('i4', 'Item 04'),
        ('i5', 'Item 05'),
        ('i6', 'Item 06'),
    )
    resp = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CHECKBOX_LIST )
    
    # Defições do Formulário
    class Meta:
        model = Formulario
        fields = '__all__'
    
    
    
    # Validações do formulário
        
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) <= 4 :
            raise forms.ValidationError('O nome deve conter mais do que 4 caracteres.')
        
        return nome
    
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        
        cpf = Formulario.returnNumero(cpf)
        
        if Formulario.verificaCPF(cpf):
            raise forms.ValidationError('O CPF deve conter no mínimo 11 digitos.')
            
        if Formulario.numeroRepetidos(cpf) >= 8:
            raise forms.ValidationError('O CPF não pode conter apenas número repetidos')
        
        return cpf
            
    def clean_ddd(self):
        ddd = self.cleaned_data['ddd']
        
        if not Formulario.verificarDdd(ddd):
            raise forms.ValidationError('O número do DDD está fora do padrão 00')
        
        return ddd
    
    def clean_telefone(self):
        tel = self.cleaned_data['telefone']
        
        if not Formulario.verificarTelefone(tel):
            raise forms.ValidationError('O número de telefone está fora do padrão 0000-0000 ou 00000-00000')
        
        return tel
        
    def clean_cep(self):
        cep = self.cleaned_data['cep']
        
        if not Formulario.verificarCep(cep):
            raise forms.ValidationError('O número de CEP está fora do padrão 00000-000')
        
        return cep