from django.shortcuts import render

from django.views.generic.list import ListView

from .models import Cars

# Create your views here.
class CarListView(ListView):
    template_name = 'index.html'
    queryset = Cars.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de productos '
        return context