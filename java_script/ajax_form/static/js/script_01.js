$(function () {                     // Aguarda a página carregar
    $("#estado").change(function () { // Associa uma função ao evento de change
        var estado = $(this).val();     // Armazena o estado selecionado
        $.ajax({                        // Inicia a definição da requisição
            url: 'filtrar_cidade/',      // Define a url da requisição
            data: {                       // Definição dos dados que serão enviados
                'estado': estado            // Adiciona dados a serem enviados
            },                            
            success: function (data) {    // Método de sucesso da requisição
                $("#cidade").html(data);    // Alimenta a dropdown list #cidades
            }
        });
    });
});