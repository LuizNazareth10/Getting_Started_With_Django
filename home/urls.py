from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from home import views as home_views

app_name = 'home'

urlpatterns = [
    path('', home_views.home, name='home'),
]
