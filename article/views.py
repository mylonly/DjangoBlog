from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from django.http import Http404
from django.template import RequestContext, loader

# Create your views here.

page_count = 5

def home(request):
    return get_posts(request,0)

def get_posts(request,page):
    page = int(page)
    post_list = Article.objects.all()[page*page_count:(page+1)*page_count]
    return render(request, 'article/home.html', {'post_list':post_list, 'page':page})

def detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExsit:
        raise Http404
    return render(request, 'article/post.html', {'post' : post})