from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('delivery-and-payment/', views.delivery_pay, name='delivery and payment'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]

