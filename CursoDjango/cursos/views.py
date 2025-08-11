# de la app cursos views.py:
from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm 
from django.shortcuts import get_object_or_404

def registrar(request):
    if request.method == 'POST':
        # Es crucial pasar request.FILES para manejar la subida de la imagen
        form = CursoForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('cursos') 
    else: # Si no es POST, se crea un formulario vacío
        form = CursoForm() 
    
    # Renderiza el formulario en la plantilla correcta (agregarCurso.html)
    # y pasa el formulario al contexto
    return render(request, 'contenido/agregarCurso.html', {'form': form})


def cursoRegistrado(request):
    cursos = Curso.objects.all()
    return render(request, 'contenido/cursos.html', {'cursos': cursos})

def eliminarCurso(request, id, confirmacion='contenido/confirmarEliminacion.html'):
    curso= get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.delete()
        cursos = Curso.objects.all()
        return render(request, "contenido/cursos.html", {'cursos': cursos})
    return render(request, confirmacion, {'object': curso})

def consultarCursoIndividual(request, id):
    curso=Curso.objects.get(id=id)
    return render(request,"contenido/formEditar.html",{'curso':curso})

def editarCurso(request, id):
    curso = get_object_or_404(Curso, id=id)
    form = CursoForm(request.POST, instance=curso)
    if form.is_valid():
        form.save() 
        cursos=Curso.objects.all()
        return render(request,"contenido/cursos.html",{'cursos':cursos})
    return render(request,"contenido/formEditar.html",{'curso':curso})

