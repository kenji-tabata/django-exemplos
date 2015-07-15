Como criar um cliente em Java no NetBeans
===

O NetBeans irá criar as classes para consumir os recursos do webservice, neste exemplo será criado as classes da 
calculadora

Crie um novo projeto em Java com qualquer nome

    Novo Projeto >> Java >> Aplicação Java

Crie um novo webservice ao clicar com o botão direito sobre o projeto Java

    Novo >> Cliente para Web Service...

Selecione a opção `WSDL URL` e digite a URL do servidor, por exemplo:

     http://soaptest.parasoft.com/calculator.wsdl

Para consumir um recurso do webservice, clique em um dos recursos da aba `Referências de Web Services` do projeto Java 
e arraste para a classe main.

    Referências de Web Services >> calculator >> Calculator >> |Calculator >> add

O método `add` será criada logo abaixo do método `main`, para utilizar o método `add` adicione no `main` as seguintes 
linhas abaixo:

```java
public static void main(String[] args) {
    float result = add(5,6);

    System.out.println(result);
}
```

Ao executar o código ele trará o resultado
```java
compile:
run:
11.0
CONSTRUÍDO COM SUCESSO (tempo total: 5 segundos)
```