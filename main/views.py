from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'main',
        'content': ['welcome to main page', 'please log in'],
        'is_authenticated': True
    }

    return render(request, 'main/index.html', context=context)
