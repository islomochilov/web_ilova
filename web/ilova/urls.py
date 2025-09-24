from django.urls import path
from .views import salom_beruvchi,all_news,detail


urlpatterns=[
    path('salom_ber/',salom_beruvchi),
    path('all_news/',all_news,name='news'),
    path('detail/<int:id>/',detail,name='detail')
]
