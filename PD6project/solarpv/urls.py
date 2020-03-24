from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.main, name='main'),
    path('portal', views.portal, name='portal'),
    path('register', views.register, name='register'),
]