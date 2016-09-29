from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import RequestContext
from django.views.debug import technical_404_response
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from SPLArch.scoping.forms import *
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from SPLArch.scoping.models import *

def lista_feature(request):
    return render(request, './features/lista_feature.html', {'forms': Feature.objects.all})

def show_feature(request, feature_id):
    form = Feature.objects.get(id=feature_id)
    form_feature = FeatureForm(instance=form)
    return render(request, './features/show_features.html', {"form_feature": form_feature})


def feature(request, feature_id):
    feature = Feature.objects.get(id=feature_id)
    form_feature = FeatureForm(instance=feature)
    cliques = feature.cliques;
    feature.cliques = cliques + 1;
    feature.save();
    return render(request, './features/cadastrar_features.html', {"form_feature": form_feature})

def cadastrarFeature(request):
    if request.method == "POST":
        form = FeatureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/lista_features')
    else:
        form = FeatureForm()

    return render(request, "./feature/cadastrar_feature.html", {'form': form}, context_instance=RequestContext(request))

class CreateFeature(CreateView):
    template_name = './features/nova_feature.html'
    model = Feature
    success_url = reverse_lazy('features')

def lista_glossary(request):
    return render(request, './glossary/lista_glossary.html', {'glossary': Glossary.objects.all})

def show_glossary(request, glossary_id):
    form = Glossary.objects.get(id=glossary_id)
    form_glossary = GlossaryForm(instance=form)
    return render(request, './glossary/show_glossary.html', {"form_glossary": form_glossary})

def glossary(request, glossary_id):
    glossary = Glossary.objects.get(id=glossary_id)
    form_glossary = GlossaryForm(instance=glossary)
    cliques = glossary.cliques;
    glossary.cliques = cliques + 1;
    glossary.save();
    return render(request, './glossary/cadastrar_glossary.html', {"form_glossary": form_glossary})

def cadastrarGlossary(request):
    if request.method == "POST":
        form = GlossaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/lista_glossary')
    else:
        form = GlossaryForm()

    return render(request, "./glossary/cadastrar_glossary.html", {'form': form},
                  context_instance=RequestContext(request))

class CreateGlossary(CreateView):
    template_name = './glossary/nova_glossary.html'
    model = Glossary
    success_url = reverse_lazy('glossary')



def lista_project(request):
    return render(request, './project/lista_project.html', {'project': Project.objects.all})

def show_project(request, project_id):
    form = Project.objects.get(id=project_id)
    form_project = ProjectForm(instance=form)
    return render(request, './project/show_project.html', {"form_project": form_project})

def project(request, project_id):
    project = Project.objects.get(id=project_id)
    form_project = ProjectForm(instance=project)
    cliques = project.cliques;
    project.cliques = cliques + 1;
    project.save();
    return render(request, './project/cadastrar_project.html', {"form_project": form_project})

def cadastrarProject(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/lista_project')
    else:
        form = ProjectForm()

    return render(request, "./project/cadastrar_project.html", {'form': form},
                  context_instance=RequestContext(request))

class CreateProject(CreateView):
    template_name = './project/nova_project.html'
    model = Project
    success_url = reverse_lazy('project')