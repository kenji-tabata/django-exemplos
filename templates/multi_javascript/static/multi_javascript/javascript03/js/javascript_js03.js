function abrir() {
    var iten = document.getElementsByTagName("input");
    if (iten) {
            for (var i=0;i<iten.length;i++) {
                    if (iten[i].name  == "principal") iten[i].onclick = seleciona;
            }
    }
}
function seleciona() {
    var el = document.form.elements; // coloque o name do Form aqui document.name-do-form
    var ql = document.form.principal.checked; // coloque aqui o nome da checkbox principal

    if (ql == true) {
            for (i=0; i<el.length; i++)
                    el[i].checked=true;
    }else {
            for (i=0; i<el.length; i++)
                    el[i].checked=false;
    }
}