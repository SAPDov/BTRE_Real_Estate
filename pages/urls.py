from django.urls import path
from . import views #. refers to the current folder

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]
