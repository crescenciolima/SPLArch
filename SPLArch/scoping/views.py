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

@login_required
def lista_feature(request):
    return render(request, './features/lista_feature.html', {'forms': Feature.objects.all})

@login_required
def show_feature(request, feature_id):
    form = Feature.objects.get(id=feature_id)
    form_feature = FeatureForm(instance=form)
    return render(request, './features/show_features.html', {"form_feature": form_feature})

@login_required
def feature(request, feature_id):
    feature = Feature.objects.get(id=feature_id)
    form_feature = FeatureForm(instance=feature)
    cliques = feature.cliques;
    feature.cliques = cliques + 1;
    feature.save();
    return render(request, './features/cadastrar_features.html', {"form_feature": form_feature})

@login_required
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

@login_required
def lista_glossary(request):
    return render(request, './glossary/lista_glossary.html', {'glossary': Glossary.objects.all})

@login_required
def show_glossary(request, glossary_id):
    form = Glossary.objects.get(id=glossary_id)
    form_glossary = GlossaryForm(instance=form)
    return render(request, './glossary/show_glossary.html', {"form_glossary": form_glossary})

@login_required
def glossary(request, glossary_id):
    glossary = Glossary.objects.get(id=glossary_id)
    form_glossary = GlossaryForm(instance=glossary)
    cliques = glossary.cliques;
    glossary.cliques = cliques + 1;
    glossary.save();
    return render(request, './glossary/cadastrar_glossary.html', {"form_glossary": form_glossary})

@login_required
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


@login_required
def lista_project(request):
    return render(request, './project/lista_project.html', {'project': Project.objects.all})

@login_required
def show_project(request, project_id):
    form = Project.objects.get(id=project_id)
    form_project = ProjectForm(instance=form)
    return render(request, './project/show_project.html', {"form_project": form_project})

@login_required
def project(request, project_id):
    project = Project.objects.get(id=project_id)
    form_project = ProjectForm(instance=project)
    cliques = project.cliques;
    project.cliques = cliques + 1;
    project.save();
    return render(request, './project/cadastrar_project.html', {"form_project": form_project})

@login_required
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


@login_required
def lista_product(request):
    return render(request, './product/lista_product.html', {'product': Product.objects.all})

@login_required
def show_product(request, product_id):
    form = Product.objects.get(id=product_id)
    form_product = ProductForm(instance=form)
    return render(request, './product/show_product.html', {"form_product": form_product})

@login_required
def product(request, product_id):
    product = Product.objects.get(id=product_id)
    form_product = ProductForm(instance=product)
    cliques = product.cliques;
    product.cliques = cliques + 1;
    product.save();
    return render(request, './product/cadastrar_product.html', {"form_product": form_product})

@login_required
def cadastrarProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/lista_product')
    else:
        form = ProductForm()

    return render(request, "./product/cadastrar_product.html", {'form': form},
                  context_instance=RequestContext(request))

class CreateProduct(CreateView):
    template_name = './product/nova_product.html'
    model = Product
    success_url = reverse_lazy('product')

@login_required
def lista_binding(request):
    return render(request, './binding/lista_binding.html', {'binding': BindingTime.objects.all})

@login_required
def show_binding(request, binding_id):
    form = BindingTime.objects.get(id=binding_id)
    form_binding = BindingForm(instance=form)
    return render(request, './binding/show_binding.html', {"form_binding": form_binding})

@login_required
def binding(request, binding_id):
    binding = BindingTime.objects.get(id=binding_id)
    form_binding = BindingForm(instance=binding)
    cliques = binding.cliques;
    binding.cliques = cliques + 1;
    binding.save();
    return render(request, './binding/cadastrar_binding.html', {"form_binding": form_binding})

@login_required
def cadastrarBinding(request):
    if request.method == "POST":
        form = BindingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/lista_binding')
    else:
        form = BindingForm()

    return render(request, "./binding/cadastrar_binding.html", {'form': form},
                  context_instance=RequestContext(request))

class CreateBinding(CreateView):
    template_name = './binding/nova_binding.html'
    model = BindingTime
    success_url = reverse_lazy('binding')