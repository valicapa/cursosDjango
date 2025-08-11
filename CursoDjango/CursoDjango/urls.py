"""
URL configuration for CursoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contenido import views
from cursos import views as views_curso
from django.conf import settings
from django.conf.urls.static import static # Necesario para servir MEDIA_URL en DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name='principal'),
    path('contacto/', views.contacto, name='contacto'),
    path('cursos/', views_curso.cursoRegistrado, name='cursos'),
    path('agregarCurso', views.agregarCurso, name='agregar'),
    path('registrar/', views_curso.registrar, name='registrar'),
    path('eliminarCurso/<int:id>/', views_curso.eliminarCurso , name='eliminar'),
    path('formEditarCurso/<int:id>/', views_curso.consultarCursoIndividual , name='ConsultaIndividual'),
    path('editarCurso/<int:id>/', views_curso.editarCurso, name='Editar'),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
