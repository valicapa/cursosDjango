from django.contrib import admin
from .models import Curso
from .models import Actividad
# Register your models here.
# class AdministrarModelo(admin.ModelAdmin):
class AdministrarCurso(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'cupoCurso', 'descripcion', 'fechaInicio')
    search_fields = ('id', 'nombre', 'cupoCurso', 'descripcion', 'fechaInicio',)
    list_filter = ( 'nombre', 'cupoCurso', )
    ordering = ('created',)
    readonly_fields = ('created', 'updated', 'id')
    date_hierarchy = 'created'

admin.site.register(Curso, AdministrarCurso)    

class AdministrarActividad(admin.ModelAdmin):
    list_display = ('id', 'nombreCurso', 'descricion', 'created')
    search_fields = ('id', 'nombreCurso', 'descricion',)
    list_filter = ('nombreCurso',)
    ordering = ('created',)
    readonly_fields = ('created', 'id')

admin.site.register(Actividad, AdministrarActividad)    