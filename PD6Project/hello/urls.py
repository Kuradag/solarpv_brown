from django.urls import path

from . import views

urlpatters = [ 
    path('hello/', views.index, name='index')
    ]