Sistema de Login do Django com Session
===

Neste exemplo é mostrado como criar uma função personalizada para o sistema de login do Django, possibilitando assim a 
utilização das SESSIONS, COOKIES e entre outros ao acessar o sistema com o login e senha.

Para testar digite os dados abaixo:

    Usuário: admin
    Senha:   123456

A função `login_user` é responsável pela conexão do sistema de login do Django e adicionar os dados na SESSION;
A função `logado` só é acessado quando o usuário estiver logado no sistema.