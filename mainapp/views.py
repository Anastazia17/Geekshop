from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')

def products(request):
    return render(request, 'mainapp/products.html')

def contact(request):
    return render(request, 'mainapp/contact.html')

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
    return render(request, 'mainapp/test_context.html', context)