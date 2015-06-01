//$(function () {
//    $("#table_list thead a").click(function (event) {
//        event.preventDefault();
//        var campo = $(this).attr("href");
//        var tipo = $(this).attr("title");
//        var tablelist = $("#table_list");
//        console.log(campo);
//        
//        if(campo.indexOf('#asc') > 0){
//            $.get("/ordem_asc/"+tipo, function (html) {
//                tablelist.remove();
//                $('body').append(html); 
//                console.log('asc');
//            }).fail(function (xhr, textStatus, error) {
//                alert(error);
//            });
//        }
//        else if(campo.indexOf('#desc') > 0){
//            $.get("/ordem_desc/"+tipo, function (html) {
//                tablelist.remove();
//                $('body').append(html); 
//                console.log('desc');
//            }).fail(function (xhr, textStatus, error) {
//                alert(error);
//            });
//        }
//        else if(campo.indexOf('#') > 0){
//            $.get("/ordem_ult/"+tipo, function (html) {
//                tablelist.remove();
//                $('body').append(html); 
//                console.log('ult');
//            }).fail(function (xhr, textStatus, error) {
//                alert(error);
//            });
//        }
//    });
//    
//    /*$("#filtro input").change(function () { 
//        tipo = $(this).attr("id");
//        console.log(tipo);
//    });*/
//});