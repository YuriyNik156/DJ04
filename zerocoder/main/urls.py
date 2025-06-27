from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('newnewnew', views.new, name="page2")
]
