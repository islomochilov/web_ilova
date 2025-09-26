from django.urls import path
from .views import salom_beruvchi,all_news,detail
from .views import YangiliklarList,KitobList,FilmList


urlpatterns=[
    path('salom_ber/',salom_beruvchi),
    path('all_news/',all_news,name='news'),
    path('detail/<int:id>/',detail,name='detail')
    
]


urlpatterns += [
    path('yangiliklar-list/',YangiliklarList.as_view(),name='yangiliklar-list')
]



urlpatterns += [
    path('kitob-list/',KitobList.as_view(),name='kitob-list')
]



urlpatterns += [
    path('film-list/',FilmList.as_view(),name='film-list')
]