from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home(request):
    print('home')

    return render(
        request,
        'home/index.html'
    )