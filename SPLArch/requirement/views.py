# Create your views here.
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.generic import CreateView
from SPLArch.requirement.models import *
from SPLArch.requirement.forms import *
from django.contrib.auth.decorators import login_required


class CreateRequirement(CreateView):
    template_name = './requirement/nova_requirement.html'
    model = Requirement
    success_url = reverse_lazy('requirement')

@login_required
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

@login_required
def requirement(request, requirement_id):
    form = Requirement.objects.get(id=requirement_id)
    form_requirement = RequirementForm(instance = form)
    cliques = form.cliques;
    form.cliques = cliques + 1
    form.save();
    return render(request, './requirement/cadastrar_requirement.html', {"form_requirement": form_requirement})

@login_required
def lista_requirement(request):
    return render(request, './requirement/lista_requirement.html', {'requirements': Requirement.objects.all})

@login_required
def show_requirements(request, requirement_id):
    register = Requirement.objects.get(id=requirement_id)
    register_form = RequirementForm(instance = register)
    return render(request, './requirement/show_requirement.html', {"register_form": register_form})

class CreateUseCase(CreateView):
    template_name = './useCase/nova_useCase.html'
    model = UseCase
    success_url = reverse_lazy('useCase')

@login_required
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

@login_required
def lista_useCase(request):
    return render(request, 'useCase/lista_useCase.html', {'uses': UseCase.objects.all})

@login_required
def show_useCases(request, use_id):
    register = UseCase.objects.get(id=use_id)
    register_form = UseCaseForm(instance = register)
    return render(request, './useCase/show_useCase.html', {"register_form": register_form})

@login_required
def useCase(request, use_id):
    form = UseCase.objects.get(id=use_id)
    form_useCase = UseCaseForm(instance = form)
    cliques = form.cliques;
    form.cliques = cliques + 1
    form.save();
    return render(request, './useCase/cadastrar_useCase.html', {"form_useCase": form_useCase})