from django.shortcuts import render
# from .models import Curso
from cursos.forms import CursoForm
# Create your views here.

def principal(request):
    return render(request, 'contenido/pagina_principal.html')


def contacto(request):
    return render(request, 'contenido/contacto.html')

def cursos(request):
    return render(request, 'contenido/cursos.html')


def agregarCurso(request):
    form = CursoForm()
    return render(request, 'contenido/agregarCurso.html', {'form': form})

