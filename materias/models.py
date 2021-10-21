from django.db import models
from datetime import date
from django.db.models.deletion import SET_NULL


class Materia(models.Model):
    """Define la tabla Materias"""
    materia = models.CharField(max_length=45)

    def __str__(self):
        """ Representación en str para usar Materia """
        return self.materia


class Tarea(models.Model):
    archivo = models.FileField()
    tema = models.CharField(max_length=45, default="Tarea", null=False, blank=False)
    comentario = models.CharField(max_length=255, null=True, blank=True)
    fecha = models.DateField(default=date.today)
    fechaLimite = models.DateField(null=True, blank=True)
    materia_tarea = models.ForeignKey(Materia, on_delete=models.CASCADE, null=False, blank=False, related_name="materia_tarea")

    def __str__(self):
        return f"{self.tema}"