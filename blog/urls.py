from blog import views as blog_views
from django.urls import path

urlpatterns = [
    path('', blog_views.index, name='index'),
    path('exemple/', blog_views.exemple, name='exemple'),
]