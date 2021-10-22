from django.db import models
from datetime import date
from django.db.models.deletion import SET_NULL
from usuarios.models import Account

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


def user_directory_path(respuesta, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/respuesta_<id>/<filename>
    return f'user_{respuesta.user.id}/respuesta_{respuesta.id}/{filename}'

class Respuesta(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, blank=False)
    materia_tarea = models.ForeignKey(Materia, on_delete=models.CASCADE, null=False, blank=False, related_name="materia_tarea2")
    tema = models.CharField(max_length=45, default="Tema", null=False, blank=False)
    comentario = models.CharField(max_length=255, null=True, blank=True)
    fecha = models.DateField(default=date.today)
    archivo = models.FileField(upload_to=user_directory_path,
                            null=True,blank=True, max_length=256)

    def __str__(self):
        return f'{self.tema}'

