import graphene

from graphene_django.types import DjangoObjectType
from .models import Aviso
from materias.models import Materia, Tarea, Respuesta
from usuarios.models import Account

# Definición de los tipos
class AvisoType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo Aviso """
    class Meta:
        # Se relaciona con el origen de la data en models.Aviso
        model = Aviso


class MateriaType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo Materia """
    class Meta:
        # Se relaciona con el origen de la data en models.Materia
        model = Materia


class TareaType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo Tarea """
    class Meta:
        # Se relaciona con el origen de la data en models.Tarea
        model = Tarea


class RespuestaType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo Respuesta """
    class Meta:
        # Se relaciona con el origen de la data en models.Respuesta
        model = Respuesta


class AccountType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo Account """
    class Meta:
        # Se relaciona con el origen de la data en models.User
        model = Account


# Creación de clases que atenderán las consultas realizadas desde el API:
class Query(graphene.ObjectType):
    """ Definición de las respuestas a las consultas posibles """

    # Se definen los posibles campos en las consultas
    all_avisos = graphene.List(AvisoType)  # allAvisos
    all_materias = graphene.List(MateriaType)  # allMateria
    all_tareas = graphene.List(TareaType)  # allTareas
    all_respuestas = graphene.List(RespuestaType)  # allRespuestas
    all_accounts = graphene.List(AccountType)  # allAccounts


    # Se define las respuestas para cada campo definido
    def resolve_all_avisos(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Aviso.objects.all()


    def resolve_all_materias(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Materia.objects.all()


    def resolve_all_tareas(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Tarea.objects.all()


    def resolve_all_respuestas(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Respuesta.objects.all()


    def resolve_all_accounts(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Account.objects.all()

# Creando mutaciones
class EliminarAccount(graphene.Mutation):
    """ Permite realizar la operación de eliminar en la tabla Account """
    class Arguments:
        """ Define los argumentos para eliminar un usuario """
        id = graphene.ID(required=True)

    # El atributo usado para la respuesta de la mutación, en este caso sólo se
    # indicará con la variuable ok true en caso de éxito o false en caso
    # contrario
    ok = graphene.Boolean()

    def mutate(self, info, id):
        """
        Se encarga de eliminar un usuario donde sólo es necesario el atributo
        id y además obligatorio.
        """
        try:
            # Si la zona existe se elimina sin más
            account = Account.objects.get(pk=id)
            account.delete()
            ok = True
        except Account.DoesNotExist:
            # Si el usuario no existe, se procesa la excepción
            ok = False
        # Se regresa una instancia de esta mutación
        return EliminarAccount(ok=ok)


class CrearMateria(graphene.Mutation):
    """ Permite realizar la operación de crear en la tabla Materia """

    class Arguments:
        """ Define los argumentos para crear un Materia """
        materia = graphene.String()

    # El atributo usado para la respuesta de la mutación
    materia = graphene.Field(MateriaType)

    def mutate(self, info, materia):
        """
        Se encarga de crear la nueva Materia
        """
        materia = Materia(
            materia=materia,
        )
        materia.save()

        # Se regresa una instancia de esta mutación y como parámetro la Materia
        # creada.
        return CrearMateria(materia=materia)

class EliminarMateria(graphene.Mutation):
    """ Permite realizar la operación de eliminar en la tabla Materia """
    class Arguments:
        """ Define los argumentos para eliminar una materia"""
        id = graphene.ID(required=True)

    # El atributo usado para la respuesta de la mutación, en este caso sólo se
    # indicará con la variuable ok true en caso de éxito o false en caso
    # contrario
    ok = graphene.Boolean()

    def mutate(self, info, id):
        """
        Se encarga de eliminar una materia donde sólo es necesario el atributo
        id y además obligatorio.
        """
        try:
            # Si la zona existe se elimina sin más
            materia = Materia.objects.get(pk=id)
            materia.delete()
            ok = True
        except Materia.DoesNotExist:
            # Si el usuario no existe, se procesa la excepción
            ok = False
        # Se regresa una instancia de esta mutación
        return EliminarMateria(ok=ok)


class Mutaciones(graphene.ObjectType):
    eliminar_account = EliminarAccount.Field()
    crear_materia = CrearMateria.Field()
    eliminar_materia = EliminarMateria.Field()


# Se crea un esquema que hace uso de la clase Query
schema = graphene.Schema(query=Query, mutation=Mutaciones)
