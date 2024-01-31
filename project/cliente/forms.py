from django import forms
from . import models

class ClienteForm(forms.ModelForm):
    class Meta:
        model =models.Cliente
        fields="__all__"

class ComentarioForm(forms.ModelForm):
    class Meta:
        model =models.Comentario
        fields="__all__"

class PublicacionForm(forms.ModelForm):
    class Meta:
        model =models.Publicacion
        fields="__all__"    
        