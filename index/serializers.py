from rest_framework import serializers

from .models import Aviso
from usuarios.models import Account
from materias.models import Materia

class MateriaSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Materia """
    class Meta:
        # Se define sobre que modelo actua
        model = Materia
        # Se definen los campos a incluir
        fields = ('id', 'materia')


class AvisoSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Aviso """
    class Meta:
        # Se define sobre que modelo actua
        model = Aviso
        # Se definen los campos a incluir
        fields = ('id', 'titulo', 'contenido', 'fecha', 'imagen')
