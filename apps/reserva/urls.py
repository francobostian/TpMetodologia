from django.conf.urls import url
from .views import index, reservaView, days, filtroView, mostrarfiltroView
urlpatterns = [
    url(r'^test$', index, name="index"),
 #   url(r'^nuevo$', propiedadView, name="propiedad_crear"),
    url(r'^crear$', reservaView, name="reserva_crear"),
    url(r'^filtro$', mostrarfiltroView, name="filtro_crear"),
    url(r'^mostrar$', filtroView, name="filtro_mostrar"),
    url(r'^days/(?P<propertyId>\d+)$', days, name="days"),
        
]
