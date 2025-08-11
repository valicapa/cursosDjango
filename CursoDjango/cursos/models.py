from django.db import models
from ckeditor.fields import RichTextField
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


class Actividad(models.Model): 
    id= models.AutoField(primary_key=True, verbose_name='Clave')
    nombreCurso=models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso al que pertenece')
    descricion = RichTextField(verbose_name='Descripcion de la ctividad')
    created= models.DateTimeField(auto_now_add=True, verbose_name='Registrado')    
    

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        ordering = ['-created']

    def __str__(self):
        return self.descricion