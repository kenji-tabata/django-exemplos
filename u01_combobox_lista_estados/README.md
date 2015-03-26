01. Django Utils: Lista dos Estados Brasileiros

Neste exemplo é mostrado como criamos uma combobox com os estados Brasileiros. O Local Flavor possuí outros tipos 
utilitários que auxiliam na validação dos campos do formulário que serão abordados em outros exemplos 

É preciso instalar o módulo LocalFlavor para alimentar a combobox com os nomes dos Estados do país.

    pip install django-localflavor

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations nome-da-model
    python manage.py migrate

Arquivos alterados ou adicionados:

    /u01_combobox_lista_estados/
        urls.py
        settings.py
        views.py
        models.py
        forms.py
    /templates/
        u01_combobox_lista_estados/
            index.html