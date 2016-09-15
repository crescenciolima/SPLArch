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
    return render(request, './api/show_api.html', {"api": api})


def nova_api(request):
    return render(request, './api/nova_api.html')


def api(request, api_id):
    api = API.objects.get(id=api_id)
    cliques = api.cliques;
    api.cliques = cliques + 1;
    api.save();
    return render(request, './api/cadastrar_api.html', {"api": api})


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


def lista_references(request):
    return render(request, './references/lista_references.html', {'references': References.objects.all})


def reference(request, reference_id):
    reference = References.objects.get(id=reference_id)
    cliques = reference.cliques;
    reference.cliques = cliques + 1
    reference.save();
    return render(request, './references/cadastrar_references.html', {"reference": reference})


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
        form = ReferencesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/lista_dssa')
    else:
        form = ReferencesForm()

    return render(request, "./references/cadastrar_references.html", {'form': form},
                  context_instance=RequestContext(request))

def cadastrarTechnologie(request):
    if request.method == "POST":
        form = ReferencesForm(request.POST, request.FILES)
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


def show_references(request, reference_id):
    reference = References.objects.get(id=reference_id)
    return render(request, './References/show_references.html', {"reference": reference})


def show_technology(request, technology_id):
    technology = Technology.objects.get(id=technology_id)
    return render(request, './technologies/show_technology.html', {"technology": technology})


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
