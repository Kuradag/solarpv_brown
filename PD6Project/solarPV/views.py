from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'solarPV/index.html')

def register(request):
    return render(request, 'solarPV/solarPV-registration.html')

def login(request):
    return render(request, 'solarPV/solarPV-login.html')