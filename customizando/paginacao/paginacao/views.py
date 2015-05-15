from django.shortcuts import render_to_response
from paginacao.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    post_list = Post.objects.order_by('id')
    paginator = Paginator(post_list, 2)
    
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    return render_to_response('paginacao/index.html', {'posts': posts})
