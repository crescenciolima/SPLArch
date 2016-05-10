# Create your views here.
from django.shortcuts import render
from SPLArch.architecture.forms import ApiForm
from SPLArch.architecture.models import Architecture, API
from django.shortcuts import render_to_response
from django.shortcuts import redirect



def home(request):
    return render(request, "tour/index.html")

def ver(request):
    return render(request, 'index.html')

def index(request):
	return render(request, 'lista_api.html', {'apis' : API.objects.filter().order_by('-cliques').distinct()[:6]})

def api(request, api_id):
    api = API.objects.get(id=api_id)
    cliques = api.cliques;
    api.cliques = cliques + 1;
    api.save();
    return render(request, 'show_api.html', {"api" : api})

def cadastrarApi(request):
    if request.method == "POST":
        form = ApiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/index')
    else:
        form = ApiForm()

    return render(request, "show_api.html", {'form': form}, context_instance=RequestContext(request))
