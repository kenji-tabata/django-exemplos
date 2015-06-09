Django Exemplos
===

Contém diversos exemplos práticos de aplicações que auxiliam no desenvolvimento de projetos desenvolvidos no Django, 
começando desde o básico ao criar uma página com "Hello World" e indo até a utilização de módulos como Reportlab e Pillow.

O Objetivo é mais para utilizar como uma fonte de informações sobre o que fazer para criar uma determinada parte do site,
como formulários, criar arquivos pdf, adicionar imagens e entre outros.


Índice
---

01. [Introdução](introducao)
02. [Templates](templates)
03. [Banco de dados](banco_de_dados)
04. [Configurando Servidor Apache](configurando_apache)
05. [Formulário: Input Types & Django Forms](input_types)
06. [Manipulando o formulário](manipulando_forms)
07. [Testes](testes)
08. [Customizando o Django](customizando)
09. [Módulos Externos](modulos_externos)



Configurações básicas utilizadas
---

Abaixo estão as configurações utilizadas no desenvolvimento dos exemplos, algumas delas já foram aplicadas neste projeto 
e estão aqui mais como informação sobre como fazer.

### Pasta padrão para os templates HTML

    1. Crie uma nova pasta na raiz do projeto com o nome `template`;
    2. Adicione no arquivo `settings.py` a seguinte configuração: `TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]`;
    3. Todo template criado deve ser colocado em uma pasta com o mesmo nome da aplicação.



### Adicionando o model da aplicação e migrando seus dados para uma database do MySQL

No arquivo `settings.py` é adicione o nome do projeto (ou aplicação) no `INSTALLED_APPS` para instalar o `model`.

    INSTALLED_APPS = (
        'django.contrib.admin',
        ...
        'nome-do-projeto'
    )

Para criar a tabela do projeto (ou aplicação) digite no terminal os seguintes comandos:

    python manage.py makemigrations nome-da-projeto
    python manage.py migrate

