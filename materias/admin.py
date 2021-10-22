from django.contrib import admin

from .models import Materia, Tarea, Respuesta

class MateriaAdmin(admin.ModelAdmin):
    # Sobre escribe lo que hace __str__
    list_display = ("id", "materia")

class TareaAdmin(admin.ModelAdmin):
    # Sobre escribe lo que hace __str__
    list_display = ("id", "user", "tema", "materia_tarea", "fecha", "fechaLimite", "comentario")


class RespuestaAdmin(admin.ModelAdmin):
    # Sobre escribe lo que hace __str__
    list_display = ("id", "user", "tema", "materia_tarea", "fecha", "comentario")

admin.site.register(Materia, MateriaAdmin)
admin.site.register(Tarea, TareaAdmin)
admin.site.register(Respuesta, RespuestaAdmin)