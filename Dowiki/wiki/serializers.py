from rest_framework import fields, serializers
from wiki.models import Articulo 
from django.core.files import File
import base64

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('__all__')