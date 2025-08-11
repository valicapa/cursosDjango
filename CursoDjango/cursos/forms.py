# your_app_name/forms.py
from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'cupoCurso', 'descripcion', 'fechaInicio', 'imagen']
        widgets = {
            'fechaInicio': forms.DateInput(attrs={'type': 'date'}),
        }