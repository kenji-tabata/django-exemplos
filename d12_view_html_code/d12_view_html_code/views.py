from django.shortcuts import render
from django.template import Context, Template


def index(request):
    lista = {'u1': "Usuário 01", 'u2': "Usuário 02", 'u3': "Usuário 03", 'u4': "Usuário 04", 'u5': "Usuário 05", 'u6': "Usuário 06"}
   
    h = Template('<p>Texto renderizado da View: {{msg}}</p>')
    
    context = Context({'msg': 'Hello World'})
    
    html = h.render(context)
        
    return render(request, 'd12_view_html_code/index.html', {'html': html})

