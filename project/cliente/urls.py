
from django.urls import path
from .views import index
from . import views

app_name = "cliente"

urlpatterns = [
    path("", views.index, name="index"),
    path("comentarios/list")
    
]
