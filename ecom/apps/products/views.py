from django.shortcuts import render
from apps.products.models import Product
from django.http import HttpResponse
# Create your views here.


def get_product(request, slug):
    try:
        context = {'product': Product.objects.get(slug=slug)}

        return render(request, 'product/products.html', context)

    except Exception as e:
        print(e)
