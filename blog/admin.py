from django.contrib import admin
from blog.models import Entrada, Comentario, Serie

# Register your models here.
admin.site.register(Entrada)
admin.site.register(Comentario)
admin.site.register(Serie)