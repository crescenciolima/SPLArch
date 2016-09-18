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


def lista_requirement(request):
    return render(request, 'useCase/lista_useCase.html', {'uses': UseCase.objects.all})


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