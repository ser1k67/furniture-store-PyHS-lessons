from unicodedata import category
from django.shortcuts import render

from catalog.models import Categories, Products

# Create your views here.
def catalog(request):
    # отображение карточек товаров
    goods = Products.objects.all()

    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }

    return render(request, "catalog/catalog.html", context=context)


def product(request, product_id):
    product = Products.objects.get(id=product_id)

    context = {
        "product": product
    }

    return render(request, "catalog/product.html", context=context)
