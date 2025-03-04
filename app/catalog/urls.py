from django.urls import path

from . import views
from catalog.models import Categories


app_name = 'catalog'

urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='catalog'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]

# добавление слагов категорий
slug_url = Categories.objects.all() 

for i in slug_url:
    urlpatterns.append(path(f'{i.slug}/', views.catalog, name=i.slug))

