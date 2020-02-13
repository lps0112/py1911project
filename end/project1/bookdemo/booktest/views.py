from django.shortcuts import render

# Create your views here.
from django.template import loader
from .models import Book, Hero
from django.http import HttpResponse


def index(request):
    # return HttpResponse("这里是<h1>首页</h1>")
    # template = loader.get_template('index.html')
    books = Book.objects.all()
    # context = {"books":books}
    # result = template.render(context)
    # return HttpResponse(result)

    return render(request, 'index.html', {"books": books})


def detail(request, bookid):
    # return HttpResponse("详情页")
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # context = {"book":book}
    # result = template.render(context)
    # return HttpResponse(result)

    return render(request, 'detail.html', {"book": book})


def about(request):
    return HttpResponse("这里是关于页")
