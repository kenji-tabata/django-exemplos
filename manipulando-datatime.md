Manipulação de data e hora
===

[https://docs.djangoproject.com/en/1.8/topics/i18n/timezones/](https://docs.djangoproject.com/en/1.8/topics/i18n/timezones/)
[https://docs.python.org/3.4/library/datetime.html#module-datetime](https://docs.python.org/3.4/library/datetime.html#module-datetime)


O `timezone` é um módulo do Django para manipular a data e hora e é considerado um atalho ou uma extensão do módulo 
`datetime` do Python. Tanto que todas as classes e funções do módulo `datetime` funcionam no módulo `timezone`.


### Configurando o Django para o fuso horário brasileiro (ao exibir no template)

Por padrão o Django trabalha somente com o fuso horário americano para a manipulação de datas(3 horas a mais com
relação ao Brasil), a alteração do fuso horário para o horário brasileiro ocorre apenas no template.

Para mudar o fuso horário do projeto altere no arquivo `mysite/app/settings.py` o valor da constante `TIME_ZONE`
com no exemplo abaixo.

```python
# mysite/app/settings.py

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
...
```


### Obter a data e hora atual

Para exibir a data e hora atual digite as linhas abaixo. O formato de saída segue o padrão americano
(ano, mês, dia, hora, minuto, segundos, micro-segundos, fuso horário):

```python
from django.utils import timezone
timezone.now()
datetime.datetime(2015, 6, 20, 18, 44, 5, 348918, tzinfo=<UTC>)
```

Ao utilizar o `print` a data atual será exibida da seguinte forma:

```python
print(timezone.now())
2015-07-07 20:20:43.067341+00:00
```

### Exibindo valores específicos do datetime

Podemos exibir apenas um valor especifico do datatime adicionado os seguintes valores após a data:

```python
timezone.now().date()           # data (2015-07-07)
timezone.now().time()           # hora (20:20:43.067341)
timezone.now().year             # ano
timezone.now().month            # mês
timezone.now().day              # dia
timezone.now().hour             # hora
timezone.now().minute           # minutos
timezone.now().second           # segundos
timezone.now().microsecond      # micro segundos
timezone.now().tzinfo           # fuso horário
```

### Manipulando a data e hora com a função `timedelta()`.

Com a função `timedelta()` podemos alterar a data atual acrescentando mais 4 semanas...

```python
from django.utils import timezone

atual = timezone.now()
print(atual)
2015-07-08 12:32:54.952816+00:00

semanas = atual + timezone.timedelta(weeks=4)
print(semana)
2015-08-05 12:32:54.952816+00:00
```

Ou voltar no tempo reduzindo a hora atual em 2 horas...

```python
horas = atual - timezone.timedelta(hours=2)
print(horas)
2015-07-08 10:32:54.952816+00:00
```

O `timedelta` aceita somente como parâmetro weeks, days, hours, minutes, seconds, miliseconds e microseconds.


### Comparando data e hora

Quando temos dois objetos do tipo datetime podemos compara-los.

```python
atual = timezone.now()
print(atual)
2015-07-08 12:32:54.952816+00:00

semanas = atual + timezone.timedelta(weeks=4)
print(semana)
2015-08-05 12:32:54.952816+00:00

if atual < semanas:
    print(True)

else:
    print(False)

True
```


### Funções úteis

Converter date para string

    timezone.now().strftime("%d/%m/%Y %H:%M:%S")
    '08/07/2015 12:46:00'


Converter string para date

    timezone.datetime.strptime("27/03/2015 7:44:55", "%d/%m/%Y %H:%M:%S")


Converter o date do Django em formato tuple

    timezone.now().timetuple()
    time.struct_time(tm_year=2015, tm_mon=7, tm_mday=8, tm_hour=12, tm_min=46, tm_sec=0, tm_wday=2, tm_yday=189, tm_isdst=0)

Converter o formato tuple em date do Django

    d_tuple = time.struct_time(tm_year=2015, tm_mon=7, tm_mday=8, tm_hour=12, tm_min=46, tm_sec=0, tm_wday=2, tm_yday=189, tm_isdst=0)
    timezone.datetime(*d_tuple[0:7])

Converter o date para o fuso horário local

    timezone.localtime(timezone.now())
    datetime.datetime(2015, 7, 8, 10, 33, 50, 287757, tzinfo=<django.utils.timezone.LocalTimezone object at 0x7f1901e008d0>)


### Funções adicionais do timezone

[https://docs.djangoproject.com/en/1.8/ref/utils/#module-django.utils.timezone](https://docs.djangoproject.com/en/1.8/ref/utils/#module-django.utils.timezone)

