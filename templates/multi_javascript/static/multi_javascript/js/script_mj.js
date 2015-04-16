$(document).ready(function(){
    $(".selecao").click(function(){
        var Campo= $(this).val();
        var inserirCampo= '<input type="text" class="'+Campo+'" name= "'+Campo+'">';
        $("#localCampo").html(inserirCampo);
        $(".cnpj").mask("99.999.999/9999-99");
        $(".cpf").mask("999.999.999-99");

    });
            
});