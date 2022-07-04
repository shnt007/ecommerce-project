from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'base/home.html')


def contact(request):
    return render(request, 'base/contact.html')


def about(request):
    return render(request, 'base/about.html')
