import os
import json

from django.shortcuts import render
from mainapp.models import Product, ProductCategory

dir = os.path.dirname(__file__)

# Create your views here.
def index(request):
    context = {'title':'GeekShop',
               'products': Product.objects.all(),
               'categories': ProductCategory.objects.all()}
    return render(request, 'mainapp/index.html', context)

def products(request, id=None):
    context = {'title': 'GeekShop - Каталог'}
    return render(request, 'mainapp/products.html', context)

def contact(request):
    context = {'title': 'GeekShop - Контакты'}
    return render(request, 'mainapp/contact.html', context)