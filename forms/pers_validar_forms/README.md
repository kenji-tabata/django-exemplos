Personalização da Validação do Django Forms
===

Neste exemplo é mostrado como criar uma validação personalizada com campos do formulário com o forms do Django. A classe 
`validar.py` contém as validações dos campos CPF, Telefone e CEP.

Para chamar cada validação no `forms.py` crie uma função com o prefixo `clean_` seguido com o mesmo nome do campo, assim 
a função será chamada automaticamente ao enviar o formulário.

Exemplo:

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) <= 4 :
            raise forms.ValidationError('O nome deve conter acima de 4 caracteres.')
        
        return nome

    A função `cleaned_data['nome']` grava na variável `nome` o valor do campo Nome do formulário;
    Faz verificação, caso o nome tenha menos que 4 caracteres é lançado a mensagem de erro;



É possível testar pelo Shell do Django as funções de validação utilizando os comandos abaixo:

# Importe o classe `validar.py`:

    from pers_validar_forms.validar import Validar

# Digite a função que deseja testar, por exemplo o telefone: 

    Validar.verificarTelefone('2345-0000')

# Para o resultado aparecer logo abaixo

    True



