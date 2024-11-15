from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from blog import views as blog_views

app_name = 'blog'

urlpatterns = [
    path('', blog_views.blog, name='blog'),
    path('exemplo/', blog_views.exemplo, name='exemplo'),
]
