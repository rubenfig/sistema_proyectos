from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^tipo/(?P<pk>[0-9]+)/$', detail_tipo_us, name='tipo_us_detail'),
    url(r'^tipo/$', list_tipo_us),
    url(r'^tipo/create/$',create_tipo),
    url(r'^tipo/delete/(?P<pk>[0-9]+)/$', delete_tipo_us, name='tipo_us_delete'),
    url(r'^tipo/update/(?P<pk>[0-9]+)/$', update_tipo_us, name='tipo_us_update'),
    url(r'^actividades/create/(?P<pk>[0-9]+)/$', create_actividad, name='actividad_create'),
    url(r'^actividades/(?P<pk>[0-9]+)/$', list_actividades, name='actividad_list'),
    url(r'^actividades/delete/(?P<pk>[0-9]+)/$', delete_actividad, name='actividad_delete'),
    url(r'^us/create/(?P<pk>[0-9]+)/$', create_us, name='us_create'),
    url(r'^us/delete/(?P<pk>[0-9]+)/$', delete_us, name='us_delete'),
    url(r'^us/update/(?P<pk>[0-9]+)/$', update_us, name='us_update'),
    url(r'^us/(?P<pk>[0-9]+)/$', detail_us, name='us_detail'),
    url(r'^us/cambiar_actividad/(?P<pk>[0-9]+)/$', cambiar_actividad, name='cambiar_actividad'),
    url(r'^us/cambiar_estado_actividad/(?P<pk>[0-9]+)/$', cambiar_estado_actividad, name='cambiar_estado_actividad'),
    url(r'^us/repriorizar/(?P<pk>[0-9]+)/$', repriorizar, name='repriorizar')

]