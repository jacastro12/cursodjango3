from tkinter import CASCADE
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
class Categorias(models.Model):
    nombres = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)

class Noticias(models.Model):
    categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    contenido = RichTextField()
