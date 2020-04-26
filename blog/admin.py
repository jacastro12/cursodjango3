
from django.contrib import admin
from .models import Noticias, Categorias
# Register your models here.

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('nombres','descripcion',)
    search_fields = ('nombres',)


class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categorias',)
    search_fields = ('nombre', )
    list_filter = ('categorias',)

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(Categorias, CategoriasAdmin)
_register(Noticias, NoticiasAdmin)
