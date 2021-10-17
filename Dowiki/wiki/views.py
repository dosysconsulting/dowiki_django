from datetime import datetime
from django.db.models import query
from django.db import connection
from django.http.response import FileResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.serializers import Serializer
from rest_framework import generics, permissions
from wiki.models import Articulo, Categoria
#from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from wiki.serializers import ArticuloSerializer, CategoriaSerializer
#from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework.parsers import MultiPartParser, FormParser
from django.utils.dateparse import parse_date, parse_datetime
from django.utils.timezone import get_current_timezone
from datetime import datetime
from django.db.models.functions import TruncMonth

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    #authentication_classes = (TokenAuthentication, )
    #permission_classes = (IsAdminUser,)
    permission_classes = (AllowAny,)
   
    @action(detail=True, methods=['POST'])
    def articulo(self, request, pk=None):
        id_articulo = pk
        titulo = request.data['titulo']
        categoria = request.data['categoria']
        descripcion = request.data['descripcion']
        try:
            articulo = Articulo.objects.get(id_articulo=id_articulo)
            articulo.titulo = titulo
            articulo.categoria = categoria
            articulo.descripcion = descripcion
            articulo.save()
            serializer = ArticuloSerializer(articulo)
            response = {'message': 'Articulo updated', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        except:
            articulo = Articulo.objects.create(id_articulo=id_articulo,
                                           titulo=titulo,
                                           categoria=categoria,
                                           descripcion= descripcion
                                               )
            serializer = ArticuloSerializer(articulo)
            response = {'message': 'Articulo created', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)

    @action(detail=True, methods=['DELETE'])
    def delete(self, request, pk=None):
        try:
            articulo = Articulo.objects.get(id_articulo=pk)
            articulo.delete()
            response = {'message': 'Articulo deleted'}
            return Response(response, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            response = {'message': 'Bad data, Articulo not exists'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    #authentication_classes = (TokenAuthentication, )
    #permission_classes = (IsAdminUser,)
    permission_classes = (AllowAny,)
   
    @action(detail=True, methods=['POST'])
    def categoria(self, request, pk=None):
        id_categoria = pk
        categoria = request.data['categoria']
        try:
            categoria = Categoria.objects.get(id_categoria=id_categoria)
            categoria.categoria = categoria
            categoria.save()
            serializer = CategoriaSerializer(categoria)
            response = {'message': 'Categoria updated', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        except:
            categoria = Categoria.objects.create(id_categoria=id_categoria,
                                           categoria=categoria
                                               )
            serializer = CategoriaSerializer(categoria)
            response = {'message': 'Categoria created', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)

    @action(detail=True, methods=['DELETE'])
    def delete(self, request, pk=None):
        try:
            categoria = Categoria.objects.get(id_categoria=pk)
            categoria.delete()
            response = {'message': 'Categoria deleted'}
            return Response(response, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            response = {'message': 'Bad data, categoria not exists'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
