from django.urls import path, include
from rest_framework import routers
from .views import *


# AGREGA UNA RUTA EN LA API 

router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)
router.register('Tipoproducto', TipoProductoViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]