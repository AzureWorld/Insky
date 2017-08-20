from django.shortcuts import render
from datetime import  datetime
from cmdb.models import Article
# Create your views here.
from django.shortcuts import HttpResponse
def index(request):
    return render(request, 'index.html', {'current_time': datetime.now()})
    #return HttpResponse("hello,world")
def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})
def base(request) :
    return render(request, 'base.html', {'current_time': datetime.now()})
def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})
def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})