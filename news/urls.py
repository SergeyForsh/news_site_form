from django.urls import path
from .views import news_list, news_create

urlpatterns = [
    path('', news_list, name='news_list'),
    path('create/', news_create, name='news_create'),
]
