from django.shortcuts import render,redirect

def index(request):
    context = {}
    
    try:
        if request.session.__contains__('exemplo'):
            context['exemplo'] = request.session['exemplo']
            print("Session encontrada: %s" % (context['exemplo']))
        else:
            context['exemplo'] = ""
    
    except KeyError as e:
        print ('A SESSION da %s não foi encontrada.' % (e))
        
    return render(request, 'try_except/index.html', context)

def del_session(request):
    try:
        del request.session['exemplo']
        print('A SESSION foi deletada!')
        
    except Exception as e:
        print ('A SESSION %s não existe.' % (e))
        
    return redirect('try_except.views.index')
    
def add_session(request):
    request.session['exemplo'] = "Exemplo de Try Except"
    print('A SESSION foi adicionada!')
    
    return redirect('try_except.views.index')