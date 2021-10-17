from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

def upload_to(instance,filename):
    return 'wiki/{filename}'.format(filename=filename)

class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length= 60,verbose_name = "Titulo") 
    imagen = models.ImageField(upload_to=upload_to, null=True,verbose_name = "Imagen del Articulo")
    categoria = models.CharField(max_length= 60,verbose_name = "Categoria") 
    descripcion = models.TextField(max_length= 1000,null= True, verbose_name = "Description")

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"

    def __str__(self):
        return self.titulo

