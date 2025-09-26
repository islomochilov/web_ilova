from django.shortcuts import render
from django.http import HttpResponse
from .models import Yangiliklar
from .models import Kitob
from.models import Film
from rest_framework import generics
from .seryalizars import YangiliklarSerializer,KitobSerializer,FilmSerializer
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



class YangiliklarList(generics.ListAPIView):
    queryset = Yangiliklar.objects.all()
    serializer_class = YangiliklarSerializer


class KitobList(generics.ListAPIView):
    queryset = Kitob.objects.all()
    serializer_class = KitobSerializer


class FilmList(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

