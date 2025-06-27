from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('create_news', views.create_news, name="add_news"),
]
