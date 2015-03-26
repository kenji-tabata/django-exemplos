from django.shortcuts import render
from django.template import Context, Template
from f10_combobox.models import Combobox

def combobox():
    lista = {'r1': "Reposta 01", 'r2': "Reposta 02", 'r3': "Reposta 03", 'r4': "Reposta 04", 'r5': "Reposta 05", 'vr6': "Reposta 06"}
   
    h = Template('<option>{{msg}}</option>')
    
    context = Context({'msg': 'Selecione um opção'})
    
    html = h.render(context)
        
    for key, value in lista.items():
        t = Template('<option>{{valor}}</option>')
        con = Context({'valor': value})
        
        html += t.render(con)
        
    return html

def index(request):
    listar_combos = Combobox.objects.order_by('id')

    html = combobox()

    return render(request, 'f10_combobox/index.html', {'html': html, 'listar_combos': listar_combos})


def enviar(request):
    listar_combos = Combobox.objects.order_by('id')
    
    html = combobox()
    
    if request.method == 'POST':
        combo = Combobox.objects.create(
            tipo = request.POST['tipo'],
        )
        return render(request, 'f10_combobox/index.html', {'html': html, 'combo': combo, 'listar_combos':listar_combos})
    
    elif request.method == 'GET':
        return render(request, 'f10_combobox/index.html', {'html': html, 'listar_combos':listar_combos})