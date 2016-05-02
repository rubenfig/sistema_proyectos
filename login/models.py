from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from cliente.models import Cliente
# Create your models here.

class Usuario (User):
    """
    Se crea la clase Usuario que hereda del modelo User de django, para agregarle mas atributos.
    cedula = numero de cedula del usuario.
    direccion = direccion del usuario.
    """
    cedula = models.PositiveIntegerField(default=0)
    direccion = models.TextField(max_length=50, blank=True, null=False)

    # Configuraciones de usuario
    hora_notificaciones = models.TimeField(null=True)
    formato_notificaciones = (
        ('html', 'HTML'),
        ('txt', 'Texto Plano')
    )
    noti_creacion_proyecto = models.BooleanField(name="Notificacion de proyectos creados",default=True)
    noti_creacion_usuario = models.BooleanField(name="Notificacion de usuarios creados",default=True)
    noti_creacion_equipos = models.BooleanField(name="Notificacion de equipos creados",default=True)

    def __unicode__(self):
        return self.username

class Telefono (models.Model):
    """
    Se crea la clase Telefono que hereda del moodelo Model de django.
    numero : Integer que representa al telefono.
    cliente : CCliente asociado al telefono.
    usuario : Usuario asociado al telefono.

    """
    numero = models.PositiveIntegerField(default=0)
    cliente = models.ForeignKey(Cliente, null=True)
    usuario = models.ForeignKey(Usuario, null=True)


    def __unicode__(self):
        return self.valor
