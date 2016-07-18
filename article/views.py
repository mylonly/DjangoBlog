from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from django.http import Http404
from django.template import RequestContext, loader

# Create your views here.

def home(request):
    post_list = Article.objects.all()
    return render(request,'article/home.html',{'post_list':post_list})

def detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExsit:
        raise Http404
    return render(request, 'post.html', {'post' : post})