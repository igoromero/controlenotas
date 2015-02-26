# -*- encoding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from models import Disciplina
from forms import FormItemDisciplina

@login_required 
def index(request):
    lista_disciplinas = Disciplina.objects.filter(usuario=request.user)

    return render(request, "lista.html",
                  {"lista_disciplinas": lista_disciplinas},context_instance=RequestContext(request))

@login_required
def adiciona(request):
    if request.method == "POST":
        form = FormItemDisciplina(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.usuario = request.user
            item.save()
            return render(request, "salvo.html", {})
    else:
        form = FormItemDisciplina()
    return render(request, "adiciona.html", {"form": form},
                  context_instance=RequestContext(request))

@login_required
def item(request, id_disciplina):
    disciplina = get_object_or_404(Disciplina, pk=id_disciplina, usuario=request.user)
    if request.method == "POST":
        form = FormItemDisciplina(request.POST, request.FILES, instance=disciplina)
        if (form.is_valid()):
            item = form.save(commit=False)
            item.usuario = request.user
            item.save()
            return render(request, "salvo.html", {})
    else:
        media = (disciplina.nota1+disciplina.nota2+disciplina.nota3)/3
        form = FormItemDisciplina(instance=disciplina)
    return render(request, "item.html",{'form': form, 'media': media}, context_instance=RequestContext(request))

@login_required
def remove(request, id_disciplina):
    disciplina = get_object_or_404(Disciplina, pk=id_disciplina, usuario=request.user)
    if(request.method == "POST"):
        disciplina.delete()
        return render(request, "removido.html", {})
    return render(request, "remove.html",{'disciplina': disciplina}, context_instance=RequestContext(request))