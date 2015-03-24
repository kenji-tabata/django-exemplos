from django.shortcuts import render
from django.template import Context, Template


def index(request):
    lista = {'r1': "Reposta 01", 'r2': "Reposta 02", 'r3': "Reposta 03", 'r4': "Reposta 04", 'r5': "Reposta 05", 'vr6': "Reposta 06"}
   
    h = Template('<option>{{msg}}</option>')
    
    context = Context({'msg': 'Selecione um opção'})
    
    html = h.render(context)
        
    for key, value in lista.items():
        t = Template('<option>{{valor}}</option>')
        con = Context({'valor': value})
        
        html += t.render(con)
    
    return render(request, 'd13_combobox_array/index.html', {'html': html})
