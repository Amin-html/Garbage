from django.shortcuts import render, HttpResponse
from .models import Car, Engine

def home(request):
    # return HttpResponse("Hello, welcome to the Cars site!")
    cars = Car.objects.all()
    return render(request, 'cars/home.html')

def cars(request):
    cars = Car.objects.all()
    engines = Engine.objects.all()
    return render(request, 'cars/cars.html', {'cars': cars, 'engines': engines})


# Create your views here.
