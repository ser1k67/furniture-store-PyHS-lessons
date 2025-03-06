from unicodedata import category
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from catalog.models import Categories, Products

# Create your views here.
def catalog(request, category_slug, page=1):
    # отображение карточек товаров по категориям
    if category_slug == "vse-tovary":
        goods = Products.objects.all()
    else:
        categories  = Categories.objects.get(slug=category_slug)
        goods = get_list_or_404(Products.objects.filter(category_id=categories.id))

    # пагинация
    paginator = Paginator(goods, 6)
    current_page = paginator.page(page) # возвращает обьекты выбранной страницы

    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "category_slug": category_slug,
    }

    return render(request, "catalog/catalog.html", context=context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
        
    context = {
        "product": product
    }

    return render(request, "catalog/product.html", context=context)
