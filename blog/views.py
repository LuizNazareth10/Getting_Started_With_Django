from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from blog.data import posts


def blog(request):
    context = {
    'text': 'Hello, Blog!',
    'posts': posts
}
    print("Posso fazer outras coisas aqui")
    return render(request, 'blog/index.html', context)

def exemplo(request):
    context = {
    'text': 'Hello, Example!',
    'title': 'Exemplo - '
}
    print("Posso fazer outras coisas aqui")
    return render(request, 'blog/exemplo.html', context)