from django.shortcuts import render

def index(request):
    return render(request, 'ajax_form/index.html', {})
