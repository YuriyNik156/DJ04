from django.urls import path
from news import views as news_views

urlpatterns = [
    path('', views.index, name="home"),
    path('create_news', news_views.create_news, name="add_news"),
]
