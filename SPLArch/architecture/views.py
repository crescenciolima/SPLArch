# Create your views here.
from django.shortcuts import render
from SPLArch.architecture.forms import ApiForm
from SPLArch.architecture.models import *
from django.shortcuts import render_to_response
from django.shortcuts import redirect

# example/app/views.py
from django.shortcuts import render

def home(request):
    return render(request, "tour/index.html")

def ver(request):
    return render(request, 'index.html')

def lista_api(request):
	return render(request, 'lista_api.html', {'apis' : API.objects.filter().order_by('-cliques').distinct()})

def show_api(request, api_id):
    api = API.objects.get(id=api_id)
    return render(request, 'show_api.html', {"api" : api})

def api(request, api_id):
    api = API.objects.get(id=api_id)
    cliques = api.cliques;
    api.cliques = cliques + 1;
    api.save();
    return render(request, 'cadastrar_api.html', {"api" : api})

def cadastrarApi(request):
    if request.method == "POST":
        form = ApiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/lista_api')
    else:
        form = ApiForm()

    return render(request, "cadastrar_api.html", {'form': form}, context_instance=RequestContext(request))


def lista_dssa(request):
	return render(request, 'lista_dssa.html', {'dssas' : DDSA.objects.all})

def lista_references(request):
	return render(request, 'lista_references.html', {'references' : References.objects.all})

def show_references(request, reference_id):
    reference = References.objects.get(id=reference_id)
    return render(request, 'show_references.html', {"reference": reference})

def new_architecture(request):
	return render(request, 'new_architecture.html')

def lista_technologies(request):
	return render(request, 'lista_technologies.html', {'technologies' : Technology.objects.all})
