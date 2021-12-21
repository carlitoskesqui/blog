
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls , name='admin'),
    path('inicio/', views.inicio, name='inicio'),
    path('login/', views.login, name='login'),
]
