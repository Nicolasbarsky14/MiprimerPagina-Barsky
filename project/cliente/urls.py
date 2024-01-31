
from django.urls import path
from . import views
app_name = "cliente"



urlpatterns = [
    path("", views.index, name="index"),

    path("clientes/list", views.clientes_list, name="clientes_list"),
    path("cliente/add", views.clientes_add, name="clientes_add"),
    path("cliente/clientes", views.Cliente, name="cliente"),
    path("cliente/publicacion_add", views.publicacion_add, name="publicacion_add"),
    path("index/list", views.publicacion_list, name="publicaciones_list"),
    path("cliente/comentarios", views.comentarios, name="comentarios"),
    path("comentarios/comentarios_listado", views.comentarios_listado, name="comentarios_listado"),
    path("cliente/comentarios_add", views.comentarios_add, name="comentarios_add"),

]

