from django.shortcuts import render

from cars.models import Car

def index(request):
    cars = Car.objects.all().order_by('-id')

    return render(request, 'index.html', {
        'message':'Listado de carros',
        'title':'Carros',
        'cars':cars
    })