from unicodedata import category
from django.shortcuts import get_list_or_404, render

from catalog.models import Categories, Products

# Create your views here.
def catalog(request, category_slug):
    # отображение карточек товаров по категориям
    if category_slug == "vse-tovary":
        goods = Products.objects.all()
    else:
        categories  = Categories.objects.get(slug=category_slug)
        goods = get_list_or_404(Products.objects.filter(category_id=categories.id))

    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }

    return render(request, "catalog/catalog.html", context=context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
        
    context = {
        "product": product
    }

    return render(request, "catalog/product.html", context=context)
