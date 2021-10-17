from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ArticuloViewSet,CategoriaViewSet

router = routers.DefaultRouter()
router.register('articulo', ArticuloViewSet)
router.register('categoria', CategoriaViewSet)

urlpatterns = [
    path('wiki/', include(router.urls)),
]