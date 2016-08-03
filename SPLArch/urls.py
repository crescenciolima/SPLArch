from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from architecture import views
from SPLArch.architecture.views import *
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
    url(r'^lista_api/', views.lista_api, name='index'),
    url(r'^lista_dssa/', views.lista_dssa, name='dssa'),
    url(r'^lista_references/', views.lista_references, name='references'),
    url(r'^cadastro/reference/', CreateReferences.as_view(), name='cadastrar_references'),
    url(r'^cadastro/technology/', CreateTechnologies.as_view(), name='cadastrar_technologies'),
    url(r'^lista_technologies/', views.lista_technologies, name='technologies'),
    url(r'^new_architecture/', views.new_architecture, name='new_architecture'),
    url(r'^cadastro/arch', views.cadastrarArc, name='cadastrarArc'),
    url(r'^tour/', 'SPLArch.architecture.views.home'),
    url(r'nova_api/', views.nova_api, name='nova_api'),
    url(r'^cadastrar_api/(?P<api_id>\d+)$', views.api, name='cadastrar_api'),
    url(r'^cadastrar_reference/(?P<reference_id>\d+)$', views.reference, name='cadastrar_reference'),
    url(r'^show_api/(?P<api_id>\d+)$', views.show_api, name='show_api'),
    url(r'^show_references/(?P<reference_id>\d+)$', views.show_references, name='show_references'),
    url(r'^show_technology/(?P<technology_id>\d+)$', views.show_technology, name='show_technologies'),
    url(r'^cadastro/api', views.cadastrarApi, name='cadastro'),
    url(r'^cadastro/references', views.cadastrarReference),
    url(r'^teste', views.ver, name='ver')


)
