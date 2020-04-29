from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {
        #Context
    })