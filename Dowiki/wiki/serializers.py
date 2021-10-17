from rest_framework import fields, serializers
from wiki.models import Articulo, Categoria
from django.core.files import File
import base64

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('__all__')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')