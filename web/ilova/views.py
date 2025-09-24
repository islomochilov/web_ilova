from django.shortcuts import render
from django.http import HttpResponse
from .models import Yangiliklar
# Create your views here.





def salom_beruvchi(request):
    return HttpResponse("assalomu aleykum guruh")





def all_news(request):
    news=Yangiliklar.objects.all()
    context={
        'news':news
    }
    return render(request,'all_news.html',context)  




def detail(request,id):
    yangilik=Yangiliklar.objects.get(id=id)
    context={
        'yangilik':yangilik
    }
    return render(request,'detail.html',context)
