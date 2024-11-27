from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Help', views.Help, name='Help'), 
    path('Contact', views.Contact, name='Contact'), 
]
