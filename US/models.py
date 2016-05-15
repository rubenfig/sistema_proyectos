from __future__ import unicode_literals

from django.db import models
from proyecto.models import Proyecto
from sprint.models import Sprint
from login.models import Usuario

# Create your models here.


class TipoUS(models.Model):
    nombre = models.TextField(default="")

    class Meta:
        permissions = (
            ("ver_tipo_US", "Puede ver tipos de US"),
            ("crear_Tipo_US", "Puede crear Tipos de US"),
        )


class Actividades(models.Model):
    nombre = models.TextField(default="")
    tipoUS = models.ForeignKey(TipoUS)

    class Meta:
        permissions = (
            ("ver_actividades", "Puede ver actividades"),
            ("crear_actividades", "Puede crear actividades"),
        )


class US(models.Model):
    proyecto = models.ForeignKey(Proyecto)
    sprint = models.ForeignKey(Sprint, null=True)
    descripcion_corta = models.TextField(default="")
    descripcion_larga = models.TextField(default="")
    tiempo_planificado = models.IntegerField(default=0)
    valor_negocio = models.IntegerField(default=0)  # 0 a 4
    urgencia = models.IntegerField(default=0)  # 0 a 4
    usuario_asignado = models.ForeignKey(Usuario)

    tipoUS = models.ForeignKey(TipoUS)

    actividad = models.ForeignKey(Actividades, limit_choices_to={'tipoUS': tipoUS})

    options_estado_actividad = (
        ('TOD', 'Todo'),
        ('DOI', 'Doing'),
        ('DON', 'Done')
    )
    estado_actividad = models.CharField(max_length=3, choices=options_estado_actividad, default='TOD')

    class Meta:
        permissions = (
            ("ver_US", "Puede ver US"),
            ("crear_US", "Puede crear US"),
        )