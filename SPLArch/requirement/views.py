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
    return render(request, 'requirement/lista_requirement.html', {'requirements': Requirement.objects.all})
