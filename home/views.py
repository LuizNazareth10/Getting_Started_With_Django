from django.shortcuts import render
# Create your views here.
context = {
    'text': 'Hello, Bia Linda!'
}
def home(request):
    return render(request, 'home/index.html', context)