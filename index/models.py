from django.db import models
from datetime import date
from usuarios.models import Account


def user_directory_path(aviso, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/aviso_<id>/<filename>
    return f'user_{aviso.user.id}/aviso_{aviso.id}/{filename}'


class Aviso(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, blank=False)
    titulo = models.CharField(max_length=45, default="Aviso", null=False, blank=False)
    contenido = models.CharField(max_length=255, null=True, blank=True)
    fecha = models.DateField(default=date.today)
    imagen = models.ImageField(upload_to=user_directory_path,
                            null=True,blank=True, max_length=256)


    def __str__(self):
        return f"{self.titulo}"