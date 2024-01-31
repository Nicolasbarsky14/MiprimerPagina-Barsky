from django.contrib import admin

# Register your models here.

from .models import Cliente,Comentario

admin.site.register(Cliente)
admin.site.register(Comentario)