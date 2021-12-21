from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path('detalle/', views.detalle, name='detalle'),
]