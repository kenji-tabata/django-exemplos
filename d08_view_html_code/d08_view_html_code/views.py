from django.shortcuts import render
from django.template import Context, Template


def index(request):
    h = Template('<p>Texto renderizado da View: {{msg}}</p>')
    
    context = Context({'msg': 'Hello World'})
    
    html = h.render(context)
        
    return render(request, 'd08_view_html_code/index.html', {'html': html})

