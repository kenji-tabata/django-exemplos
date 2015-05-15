$(function () {
    $("#formulario").submit(function (event) {
        event.preventDefault();
        
        var userlist = $("#content");
        $.post("/enviar/", $(this).serialize(), function (html) {
            userlist.remove();
            $('body').append(html);
        }).fail(function (xhr, textStatus, error) {
            alert(error);
        });
    });
    
    $("#comment").submit(function (event) {
        event.preventDefault();
                
        var jsonUser = {
            usuario: $("select[name='usuario']").val(),
            assunto: $("input[name='assunto']").val(),
            data: $("input[name='data']").val(),
            msg: $("textarea[name='msg']").val()
        };
        
        var userlist = $("#content");
        $.post("/enviar_comentario/", "comentario="+ JSON.stringify(jsonUser), function (html) {
            userlist.remove();
            $('body').append(html);
        }).fail(function (xhr, textStatus, error) {
            alert(error);
        });
    });
});


