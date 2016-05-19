# Create your views here.
from django.shortcuts import render
from SPLArch.architecture.forms import ApiForm
from SPLArch.architecture.models import Architecture, API
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
