from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from architecture import views
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
    url(r'^tour/', 'SPLArch.architecture.views.home'),
    url(r'^cadastrar_api/(?P<api_id>\d+)$', views.api, name='cadastrar_api'),
    url(r'^cadastro/api', views.cadastrarApi, name='cadastro'),
    url(r'^teste', views.ver, name='ver')


)
