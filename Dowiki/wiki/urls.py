from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ArticuloViewSet

router = routers.DefaultRouter()
router.register('articulo', ArticuloViewSet)

urlpatterns = [
    path('wiki/', include(router.urls)),
]