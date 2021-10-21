from django.contrib import admin

from .models import Materia, Tarea

class MateriaAdmin(admin.ModelAdmin):
    # Sobre escribe lo que hace __str__
    list_display = ("id", "materia")

class TareaAdmin(admin.ModelAdmin):
    # Sobre escribe lo que hace __str__
    list_display = ("id", "tema", "comentario", "fecha", "fechaLimite", "materia_tarea")


admin.site.register(Materia, MateriaAdmin)
admin.site.register(Tarea, TareaAdmin)