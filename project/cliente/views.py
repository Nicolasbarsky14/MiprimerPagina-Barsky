from django.shortcuts import render, redirect
from . import models
from . import forms

# Create your views here.
def index(request):
    return render(request, "cliente/index.html")

def Cliente(request):
    return render(request, "cliente/clientes.html")

def clientes_list(request):
    clientes = models.Cliente.objects.all()
    contexto = {"autores": clientes}
    return render(request, "cliente/clientes_list.html", contexto)

def clientes_add(request):
    if request.method == "Publicacion":
        form = forms.ClienteForm(request.Publicacion)
        if form.is_valid():
            form.save()
            return redirect("cliente:clientes_list")
    else:
        form = forms.ClienteForm
    return render(request, "cliente/clientes_add.html", {"form": form})

def comentarios(request):
    return render(request, "cliente/comentarios.html")

def comentarios_listado(request):
    comentario = models.Comentario.objects.all()
    contexto = {"comentario": comentario}
    return render(request, "cliente/comentarios_listado.html", contexto)

def comentarios_add(request):
    if request.method == "Publicacion":
        form = forms.ComentarioForm(request.Publicacion)
        if form.is_valid():
            form.save()
            return redirect("cliente:comentarios_listado")
    else:
        form = forms.ComentarioForm
    return render(request, "cliente/comentarios_add.html", {"form": form})

def publicacion_list(request):
    publicacion = models.Publicacion.objects.all()
    contexto = {"Publicacion": publicacion }
    return render(request, "cliente/publicacion_list.html", contexto)
 
def publicacion_add(request):
    if request.method == "Publicacion":
        form = forms.PublicacionForm(request.Publicacion)
        if form.is_valid():
            form.save()
            return redirect("cliente:publicacion_listado")
    else:
        form = forms.PublicacionForm
    return render(request, "cliente/publicacion_Add.html", {"form": form})

