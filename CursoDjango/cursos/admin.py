from django.contrib import admin
from .models import Curso

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