from django.shortcuts import render
from apps.products.models import Product

# Create your views here.


def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'home/home.html', context)


def contact(request):
    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')
