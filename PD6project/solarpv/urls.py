from django.urls import path

from . import views

app_name = 'solarpv'

urlpatterns = [
    path('', views.main, name='main'),
    path('portal', views.portal, name='portal'),
    path('register', views.register, name='register'),
]