from django.db import models

# Create your models here.

class Curso(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID del curso')
    nombre = models.CharField(max_length=20, verbose_name='Nombre del curso')
    cupoCurso = models.IntegerField(verbose_name='Cupo del curso')
    descripcion = models.TextField(verbose_name='Descripción del curso')
    fechaInicio = models.DateField(verbose_name='Fecha de inicio')
    imagen = models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografia')    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['created'] 
    def __str__(self):
        return self.nombre
        