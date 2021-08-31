from django.urls import path
from . import views 

urlpatterns = [
    path('', views.contact, name='contact'),
    path('delete/<int:listing_id>', views.delete, name='delete'),]

