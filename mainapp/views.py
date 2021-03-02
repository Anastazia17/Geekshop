from django.shortcuts import render
import os
import json

dir = os.path.dirname(__file__)

# Create your views here.
def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {'title': 'GeekShop - Каталог'}
    return render(request, 'mainapp/products.html', context)

def contact(request):
    context = {'title': 'GeekShop - Контакты'}
    return render(request, 'mainapp/contact.html', context)

def test_context(request):
    context = {
        'title': 'geekshop',
        'header': 'Добро пожаловать на сайт!',
        'username': 'Анастасия Цыбусова',
        'products': [
            {'name': 'Отличный стул', 'price': '2585.90'},
            {'name': 'Настольная лампа', 'price': '1990.00'},
            {'name': 'Люстра Модерн', 'price': '3450.00'},
        ],
        'products_of_promotion': [
            {'name': 'Отличный стул 2', 'price': '2100.99'},
            {'name': 'Настольная лампа 2', 'price': '1500.99'},
        ],
    }
    file_path = os.path.join(dir, 'fixtures/products.json')
    context.update(json.load(open(file_path, encoding='utf-8')))
    return render(request, 'mainapp/test_context.html', context)