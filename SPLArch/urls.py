from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from architecture import views
from SPLArch.architecture.views import *
from SPLArch.requirement.views import lista_requirement, CreateRequirement, cadastrarRequirement, \
    lista_useCase, CreateUseCase, cadastrarUseCase, show_requirements, show_useCases, useCase, requirement
from SPLArch.scoping.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'core.views.home', name='home'),
    # url(r'^core/', include('core.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
     url(r'^$', include(admin.site.urls)),
    url('^faq/', include('SPLArch.faq.urls')),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url':'/login/'}, name='logout'),

    url(r'^lista_api/', views.lista_api, name='index'),
    url(r'nova_api/', views.nova_api, name='nova_api'),
    url(r'^cadastrar_api/(?P<api_id>\d+)$', views.api, name='cadastrar_api'),
    url(r'^show_api/(?P<api_id>\d+)$', views.show_api, name='show_api'),
    url(r'^cadastro/api', views.cadastrarApi, name='cadastro'),


    url(r'^lista_dssa/', views.lista_dssa, name='dssa'),
    url(r'^cadastro/dssa/', CreateDSSA.as_view(), name='cadastrar_dssa'),
    url(r'^cadastro/dssas', views.cadastrarDSSA),


   url(r'^cadastro/technology/', CreateTechnologies.as_view(), name='cadastrar_technologies'),
   url(r'^cadastro/technologies', views.cadastrarTechnologie),
   url(r'^lista_technologies/', views.lista_technologies, name='technologies'),
   url(r'^cadastrar_technology/(?P<technology_id>\d+)$', views.technology, name='cadastrar_technology'),
   url(r'^show_technology/(?P<technology_id>\d+)$', views.show_technology, name='show_technologies'),


    url(r'^lista_references/', views.lista_references, name='references'),
    url(r'^cadastro/reference/', CreateReferences.as_view(), name='cadastrar_references'),
    url(r'^cadastrar_reference/(?P<reference_id>\d+)$', views.reference, name='cadastrar_reference'),
    url(r'^show_references/(?P<reference_id>\d+)$', views.show_references, name='show_references'),
    url(r'^cadastro/references', views.cadastrarReference),

    url(r'^lista_scenarios/', views.lista_scenario, name='scenarios'),
    url(r'^cadastro/scenario/', CreateScenario.as_view(), name='cadastrar_scenarios'),
    url(r'^cadastrar_scenario/(?P<scenario_id>\d+)$', views.scenario, name='cadastrar_scenario'),
    url(r'^show_scenarios/(?P<scenario_id>\d+)$', views.show_scenarios, name='show_scenarios'),
    url(r'^cadastro/scenario', views.cadastrarScenario),


    url(r'^lista_requirements/', lista_requirement, name='requirements'),
    url(r'^cadastro/requirement/', CreateRequirement.as_view(), name='cadastrar_requirement'),
    url(r'^cadastro/requirements', cadastrarRequirement),
     url(r'^cadastrar_requirement/(?P<requirement_id>\d+)$', requirement, name='cadastrar_requirement'),
     url(r'^show_requirements/(?P<requirement_id>\d+)$', show_requirements, name='show_requirements'),

    url(r'^lista_features/', lista_feature, name='features'),
    url(r'^cadastro/feature/', CreateFeature.as_view(), name='cadastrar_feature'),
    url(r'^cadastro/features', cadastrarFeature),
    url(r'^cadastrar_feature/(?P<feature_id>\d+)$', feature, name='cadastrar_feature'),
   url(r'^show_feature/(?P<feature_id>\d+)$', show_feature, name='show_feature'),

   url(r'^lista_glossary/', lista_glossary, name='glossary'),
   url(r'^cadastro/glossary/', CreateGlossary.as_view(), name='cadastrar_glossary'),
   url(r'^cadastro/glossarys', cadastrarGlossary),
   url(r'^cadastrar_glossary/(?P<glossary_id>\d+)$', glossary, name='cadastrar_glossary'),
   url(r'^show_glossary/(?P<glossary_id>\d+)$', show_glossary, name='show_glossary'),

   url(r'^lista_requirements/', lista_requirement, name='requirements'),
   url(r'^cadastro/requirement/', CreateRequirement.as_view(), name='cadastrar_requirement'),
   url(r'^cadastro/requirements', cadastrarRequirement),
   url(r'^cadastrar_requirement/(?P<requirement_id>\d+)$', requirement, name='cadastrar_requirement'),
   url(r'^show_requirements/(?P<requirement_id>\d+)$', show_requirements, name='show_requirements'),

   url(r'^lista_project/', lista_project, name='project'),
   url(r'^cadastro/project/', CreateProject.as_view(), name='cadastrar_project'),
   url(r'^cadastro/projects', cadastrarProject),
   url(r'^cadastrar_project/(?P<project_id>\d+)$', project, name='cadastrar_project'),
   url(r'^show_project/(?P<project_id>\d+)$', show_project, name='show_project'),

   url(r'^lista_product/', lista_product, name='product'),
   url(r'^cadastro/products/', CreateProduct.as_view(), name='cadastrar_product'),
   url(r'^cadastro/products', cadastrarProduct),
   url(r'^cadastrar_product/(?P<product_id>\d+)$', product, name='cadastrar_product'),
   url(r'^show_product/(?P<product_id>\d+)$', show_product, name='show_product'),

   url(r'^lista_binding/', lista_binding, name='binding'),
   url(r'^cadastro/bindings/', CreateBinding.as_view(), name='cadastrar_binding'),
   url(r'^cadastro/bindings', cadastrarBinding),
   url(r'^cadastrar_binding/(?P<binding_id>\d+)$', binding, name='cadastrar_binding'),
   url(r'^show_binding/(?P<binding_id>\d+)$', show_binding, name='show_binding'),

   url(r'^lista_useCases/', lista_useCase, name='useCase'),
   url(r'^cadastro/useCase/', CreateUseCase.as_view(), name='cadastrar_useCase'),
   url(r'^cadastro/useCases', cadastrarUseCase),
   url(r'^cadastrar_useCase/(?P<use_id>\d+)$', useCase, name='cadastrar_useCase'),
   url(r'^show_useCase/(?P<use_id>\d+)$', show_useCases, name='show_useCases'),

    url(r'^new_architecture/', cad_Arc, name='new_architecture'),
    url(r'^cadastro/arch', views.cadastrarArc, name='cadastrarArc'),



    url(r'^tour/', 'SPLArch.architecture.views.home'),




    url(r'^teste', views.ver, name='ver')


)
