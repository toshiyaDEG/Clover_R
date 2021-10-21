from django.contrib import admin
from .models import Aviso

class AvisoAdmin(admin.ModelAdmin):
    # Sobre escribe lo que hace __str__
    list_display = ("id", "user", "titulo", "contenido", "imagen", "fecha", "user")

admin.site.register(Aviso, AvisoAdmin)
