Utilizando a constate nos arquivos Python
===

O arquivo `settings.py` permite definir constantes para utilização em qualquer arquivo Python do projeto. 

```python
# trecho do arquivo settings.py
SUA_CONSTANTE = [os.path.join(BASE_DIR, '/uma/pasta/qualquer/')]
```


```python
from django.conf import settings

#
# Podemos simplesmente imprimir o valor
#
print(SUA_CONSTANTE)

#
# Um exemplo interessante é na referência a arquivos
#
print ('%s/foo.txt' % settings.SUA_CONSTANTE)
```