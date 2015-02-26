from django import forms
from models import Disciplina

class FormItemDisciplina(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ('nome', 'nota1', 'nota2', 'nota3')
