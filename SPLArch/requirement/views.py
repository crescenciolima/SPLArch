# Create your views here.
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.generic import CreateView
from SPLArch.requirement.models import *
from SPLArch.requirement.forms import *


class CreateRequirement(CreateView):
    template_name = './requirement/nova_requirement.html'
    model = Requirement
    success_url = reverse_lazy('requirement')

def cadastrarRequirement(request):
    if request.method == "POST":
        form = RequirementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/lista_requirements')
    else:
        form = RequirementForm()

    return render(request, "./references/cadastrar_references.html", {'form': form},
                  context_instance=RequestContext(request))

def requirement(request, requirement_id):
    form = Requirement.objects.get(id=requirement_id)
    form_requirement = RequirementForm(instance = form)
    cliques = form.cliques;
    form.cliques = cliques + 1
    form.save();
    return render(request, './requirement/cadastrar_requirement.html', {"form_scenario": form_requirement})

def lista_requirement(request):
    return render(request, './requirement/lista_requirement.html', {'requirements': Requirement.objects.all})

def show_requirements(request, requirement_id):
    register = Requirement.objects.get(id=requirement_id)
    register_form = RequirementForm(instance = register)
    return render(request, './requirement/show_requirement.html', {"register_form": register_form})

class CreateUseCase(CreateView):
    template_name = './useCase/nova_useCase.html'
    model = UseCase
    success_url = reverse_lazy('useCase')

def cadastrarUseCase(request):
    if request.method == "POST":
        form = UseCaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/lista_useCases')
    else:
        form = UseCaseForm()

    return render(request, "./references/cadastrar_references.html", {'form': form},
                  context_instance=RequestContext(request))


def lista_useCase(request):
    return render(request, 'useCase/lista_useCase.html', {'uses': UseCase.objects.all})

def show_useCases(request, use_id):
    register = UseCase.objects.get(id=use_id)
    register_form = UseCaseForm(instance = register)
    return render(request, './useCase/show_useCase.html', {"register_form": register_form})

def useCase(request, use_id):
    form = UseCase.objects.get(id=use_id)
    form_useCase = UseCaseForm(instance = form)
    cliques = form.cliques;
    form.cliques = cliques + 1
    form.save();
    return render(request, './useCase/cadastrar_useCase.html', {"form_useCase": form_useCase})