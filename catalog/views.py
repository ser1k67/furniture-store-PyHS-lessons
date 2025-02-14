from django.shortcuts import render


# Create your views here.
def catalog(request):
    return render(request, 'catalog/catalog.html')

def product(request):
    return render(request, 'catalog/product.html')