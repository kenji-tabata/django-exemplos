$(function () {
    $("#table_list thead a").click(function () {
        var campo = $(this).attr("href");
        var tipo = $(this).attr("title");
        var tablelist = $("#table_list");
        
        if(campo=="#asc"){
            $.get("/ordem_asc/", "tipo="+tipo, function (html) {
                tablelist.remove();
                $('body').append(html); 
            }).fail(function (xhr, textStatus, error) {
                alert(error);
            });
        }
        else if(campo=="#desc"){
            $.get("/ordem_desc/", "tipo="+tipo, function (html) {
                tablelist.remove();
                $('body').append(html);
            }).fail(function (xhr, textStatus, error) {
                alert(error);
            });
        }
        else if(campo=="#"){
            $.get("/ordem_ult/", "tipo="+tipo, function (html) {
                tablelist.remove();
                $('body').append(html);
            }).fail(function (xhr, textStatus, error) {
                alert(error);
            });
        }
    });
    
    /*$("#filtro input").change(function () { 
        tipo = $(this).attr("id");
        console.log(tipo);
    });*/
});