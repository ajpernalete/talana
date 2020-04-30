from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Car

# Create your views here.
class CarListView(ListView):
    template_name = 'index.html'
    queryset = Car.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de carros'
        #print(context)
        return context

class CarDetailList(DetailView): #id -> pk
    model = Car
    template_name = 'cars/car.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(context)
        return context