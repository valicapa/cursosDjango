from django.shortcuts import render
from .models import Curso
# Create your views here.

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/cursos.html')