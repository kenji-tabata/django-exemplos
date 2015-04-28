Django Forms: Auto Validar
===

Neste exemplo é mostrado como utilizar a classe Forms do Django para criar formulários baseado no model da aplicação.

O objetivo é validar todos os campos do formulário, caso encontre algum campo que esteja em branco mostra um erro e não 
envia as informações. O método save() irá somente gravar caso todos os campos estejam preenchidos. 