Separando código de Java Script por aplicações e projetos
===

Exemplo de uma estrutura de arquivos com pequenos códigos de Javascripts separados por projeto e aplicação.

Os scripts da pasta `static/js` são carregados em todos os templates do projeto;

Os scripts da pasta `static/multi_javascript/js` são carregados em todos os templates do projeto `multi_javascript`;

Os scripts da pasta `static/multi_javascript/javascript01/js` são carregados apenas nos templates da aplicação `javascript01`.

A estrutura é apenas um exemplo de como organizar a pasta static relacionando os arquivos para cada aplicação e compartilhando 
aqueles que podem ser utilizadas em todas as aplicações do projeto.

Esta estrutura não impede de uma aplicação carregar o Javascript de uma outra aplicação, desde que estejam na mesma pasta 
do projeto. Por exemplo, o template `pagina` do projeto `multi_javascript` pode carregar o Javascript da aplicação 
`javascript01`.

