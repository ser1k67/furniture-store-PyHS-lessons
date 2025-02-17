from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Categories

# index page
def index(request):
    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная страница',
        'content': 'Магазин мебели HOME',
        'categories': categories,
    }

    return render(request, 'main/index.html', context=context)

# delivery and payment page
def delivery_pay(request):
    context = {
        'title': 'Home - Доставка и оплата',
        'content': 'Доставляем и оплачиваем, мы молодцы'
    }

    return render(request, 'main/delivery and payment.html', context=context)

# contacts page
def contact(request):
    context = {
        'title': 'Home - Контакты',
        'content': '87023280874, serikbaynazarali@gmail.com'
    }

    return render(request, 'main/contact.html', context=context)

# about page
def about(request):
    context = {
        'title': 'Home - Про нас',
        'content': 'Мы очень крутая компания по пройзводству мебели'
    }

    return render(request, 'main/about.html', context=context)
