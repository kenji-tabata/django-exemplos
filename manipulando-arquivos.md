Manipulação de arquivo
===

Leitura e escrita.


```python
arquivo = open("%s" % "foo.txt", "r")

for linha in arquivo.readlines():
    print(linha)

arquivo.write("conteúdo")
arquivo.close()
```

Se criarmos um arquivos que não existe basta...

```python
arquivo = open("%s" % "foo.txt", "w")
arquivo.close()
```

Para abrir e adicionar conteúdo...

arquivo_r = open("%s" % "foo.txt", "r")
arquivo_w = open("%s" % "foo.txt", "w")
arquivo_w.write(arquivo_r + "conteúdo adicional")

Para remover arquivo.

os.remove("%s" % "foo.txt")
