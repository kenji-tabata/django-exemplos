Visualizar mensagens no log do servidor
===


Assim como o Javascript possui o `console.log` para exibir erros e resultados, o Django permite 
também a visualização de erros e resultados em seu terminal ou no log de erros do Apache.

Por padrão todas as mensagens de erros do Django já são visualizadas no servidor do Django.

No servidor Apache as mensagens de erros são salvas no arquivo `/var/log/apache2/error.log` (Debian).

Por exemplo, para visualizar o resultado de uma função ou o conteúdo de uma variável com o `print`:

    foo = 'Uma string...'

    print (foo)

Resultado no servidor embutido

    Uma string...

Resultado no Log do servidor Apache

    [Mon Jun 15 11:34:46 2015] [error] Uma string...

