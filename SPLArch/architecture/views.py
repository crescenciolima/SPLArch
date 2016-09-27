# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import RequestContext
from django.views.debug import technical_404_response

from SPLArch.architecture.forms import *
from SPLArch.architecture.models import *
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from SPLArch.component.models import *

# example/app/views.py
from django.shortcuts import render


def home(request):
    return render(request, "tour/index.html")


def ver(request):
    return render(request, 'index.html')

@login_required
def lista_api(request):
    return render(request, './api/lista_api.html', {'apis': API.objects.filter().order_by('-cliques').distinct()})

def login(request):
    return render(request, "../templates/login.html")

def show_api(request, api_id):
    api = API.objects.get(id=api_id)
    form_api = ApiForm(instance=api)
    return render(request, './api/show_api.html', {"form_api": form_api})

def show_references(request, reference_id):
    reference = References.objects.get(id=reference_id)
    reference_form = ReferencesForm(instance = reference)
    return render(request, './references/show_references.html', {"reference_form": reference_form})

def show_scenarios(request, scenario_id):
    register = Scenarios.objects.get(id=scenario_id)
    register_form = ScenariosForm(instance = register)
    return render(request, './scenario/show_scenario.html', {"register_form": register_form})

def show_technology(request, technology_id):
    technology = Technology.objects.get(id=technology_id)
    technology_form = TechnologyForm(instance = technology)
    return render(request, './technologies/show_technology.html', {"technology_form": technology_form})

def nova_api(request):
    return render(request, './api/nova_api.html')


def api(request, api_id):
    api = API.objects.get(id=api_id)
    form_api = ApiForm(instance=api)
    cliques = api.cliques;
    api.cliques = cliques + 1;
    api.save();
    return render(request, './api/cadastrar_api.html', {"form_api": form_api})


def cadastrarApi(request):
    if request.method == "POST":
        form = ApiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/lista_api')
    else:
        form = ApiForm()

    return render(request, "./api/cadastrar_api.html", {'form': form}, context_instance=RequestContext(request))


def lista_dssa(request):
    return render(request, 'dssa/lista_dssa.html', {'dssas': DDSA.objects.all})

def lista_scenario(request):
    return render(request, './scenario/lista_scenario.html', {'scenarios':Scenarios.objects.all})


def lista_references(request):
    return render(request, './references/lista_references.html', {'references': References.objects.all})


class CreateScenario(CreateView):
    template_name = './scenario/nova_scenario.html'
    model = Scenarios
    success_url = reverse_lazy('scenarios')

def cadastrarScenario(request):
    if request.method == "POST":
        form = ScenariosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/lista_scenarios')
    else:
        form = ScenariosForm()

    return render(request, "./references/cadastrar_references.html", {'form': form},
                  context_instance=RequestContext(request))

def reference(request, reference_id):
    reference = References.objects.get(id=reference_id)
    form_reference = ReferencesForm(instance = reference)
    cliques = reference.cliques;
    reference.cliques = cliques + 1
    reference.save();
    return render(request, './references/cadastrar_references.html', {"form_reference": form_reference})

def scenario(request, scenario_id):
    form = Scenarios.objects.get(id=scenario_id)
    form_scenario = ScenariosForm(instance = form)
    cliques = form.cliques;
    form.cliques = cliques + 1
    form.save();
    return render(request, './scenario/cadastrar_scenario.html', {"form_scenario": form_scenario})

def technology(request, technology_id):
    technology = Technology.objects.get(id=technology_id)
    form_technology = TechnologyForm(instance = technology)
    cliques = technology.cliques;
    technology.cliques = cliques + 1
    technology.save();
    return render(request, './technologies/cadastrar_technology.html', {"form_technology": form_technology})

class CreateReferences(CreateView):
    template_name = './references/nova_reference.html'
    model = References
    success_url = reverse_lazy('references')

class CreateTechnologies(CreateView):
    template_name = './technologies/nova_technology.html'
    model = Technology
    success_url = reverse_lazy('technologies')

class CreateDSSA(CreateView):
    template_name = './dssa/nova_dssa.html'
    model = DDSA
    success_url = reverse_lazy('technologies')

def cadastrarDSSA(request):
    if request.method == "POST":
        form = DSSAForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/lista_dssa')
    else:
        form = ReferencesForm()

    return render(request, "./references/cadastrar_references.html", {'form': form},
                  context_instance=RequestContext(request))

def cadastrarTechnologie(request):
    if request.method == "POST":
        form = TechnologyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/lista_technologies')
    else:
        form = ReferencesForm()

    return render(request, "./references/cadastrar_references.html", {'form': form},
                  context_instance=RequestContext(request))


def cadastrarReference(request):
    if request.method == "POST":
        form = ReferencesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/lista_references')
    else:
        form = ReferencesForm()

    return render(request, "./references/cadastrar_references.html", {'form': form},
                  context_instance=RequestContext(request))

def cad_architecture(request):
    if request.method == "POST":
        form = ApiForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']

    else:
        form = ApiForm()

    return render(request, "new_architecture.html", {'form': form}, context_instance=RequestContext(request))


def cadastrarArc(request):
    if request.method == "POST":
        name = request.cleaned_data['name']
        print(name)
    else:
        form = ApiForm()

    return render(request, "new_architecture.html", {'form': form}, context_instance=RequestContext(request))


def new_architecture(request):
    return render(request, 'new_architecture.html', {'apis': API.objects.filter().order_by('-cliques').distinct(),
                                                     'references': References.objects.all})


def lista_technologies(request):
    return render(request, './technologies/lista_technologies.html', {'technologies': Technology.objects.all})


def lista_featureBinding(request):
    return render(request, './scoping/lista_featureBinding.html', {'uses': Feature.objects.all})