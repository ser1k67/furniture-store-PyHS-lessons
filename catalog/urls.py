from django.urls import path

from . import views
from catalog.models import Categories


app_name = 'catalog'

urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>/', views.catalog, name='catalog'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]
