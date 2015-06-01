Configurando AJAX com CSRF POST do Django
===

Todas as requisições POST do Django utilizam a chave de segurança CSRF ao enviar as informações dos formulários para 
prevenir ataques de Cross-Site Request Forgery.

Em formulários do template inserimos a TAG {% csrf_token %} para o método POST funcionar, ao utilizar o método POST do 
AJAX é preciso criar um arquivo .js com as configurações abaixo para enviar a chave CSRF.    

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });


[Saiba mais sobre CSRF](http://www.redesegura.com.br/2012/03/serie-ataques-os-ataques-cross-site-request-forgery-csrf/).