from django.shortcuts import HttpResponse, render
from django.template import loader

# Create your views here.

def main(request):
    return render(request, 'solarpv/main.html')

def portal(request):
    return render(request, 'solarpv/portal.html')

def register(request):
    return render(request, 'solarpv/register.html')