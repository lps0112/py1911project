from django.shortcuts import render,redirect,reverse

# Create your views here.
from django.template import loader
from .models import Book, Hero
from django.http import HttpResponse


def index(request):
    # return HttpResponse("这里是 <h1>首页</h1> ")

    # template = loader.get_template('index.html')
    books = Book.objects.all()
    # context = {"books": books}
    # result = template.render(context)
    # 3将渲染结果使用httpresponse返回
    # return HttpResponse(result)

    # 3合1
    return render(request,'index.html',{"books":books})

def detail(request,bookid):
    # return HttpResponse("这里是详情页"+bookid)
    # template = loader.get_template('detail.html')
    book  = Book.objects.get(id=bookid)
    # context = {"book":book}
    # result = template.render(context)
    # return HttpResponse(result)

    return render(request,'detail.html',{"book":book})

def deletebook(request,bookid):
    book = Book.objects.get(id=bookid)
    book.delete()
    # return HttpResponse("删除成功")
    # return HttpResponseRedirect(redirect_to='/')
    url = reverse("booktest:index")
    # return redirect(to="/")
    return redirect(to=url)

def addhero(request,bookid):
    if request.method == "GET":
        return render(request,'addhero.html')
    elif request.method == "POST":
        hero = Hero()
        hero.name = request.POST.get("heroname")
        hero.content = request.POST.get("herocontent")
        hero.gender = request.POST.get("sex")
        hero.book = Book.objects.get(id=bookid)
        hero.save()
        url = reverse("booktest:detail",args=(bookid,))
        return  redirect(to=url)


def edithero(request,heroid):
    hero = Hero.objects.get(id=heroid)
    if request.method == "GET":
        return render(request,'edithero.html',{"hero":hero})
    elif request.method == "POST":
        hero.name = request.POST.get("heroname")
        hero.content = request.POST.get("herocontent")
        hero.gender = request.POST.get("sex")
        hero.save()
        url = reverse("booktest:detail",args=(hero.book.id,))
        return redirect(to=url)


def deletehero(request,heroid):
    hero = Hero.objects.get(id=heroid)
    bookid = hero.book.id
    hero.delete()

    url = reverse("booktest:detail",args=(bookid,))
    return redirect(to=url)


def about(request):
    return HttpResponse("这里是关于")


