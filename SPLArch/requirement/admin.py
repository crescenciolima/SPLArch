from SPLArch.requirement.forms import *
from django.contrib import admin
from django.forms import Textarea
from SPLArch.requirement.models import*
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext as _
from SPLArch.scoping.forms import *
from SPLArch.architecture.models import *
from django.contrib import admin
from SPLArch.scoping.models import Feature, Product, Glossary, Project, BindingTime
from SPLArch.requirement.models import *
from django.forms import *
from mptttreewidget.widget import MpttTreeWidget
from django.shortcuts import render_to_response
from django.utils.translation import ugettext as _
from django.utils.encoding import force_unicode
from django.template import RequestContext
from django.http import HttpResponse
from django.core.files.temp import NamedTemporaryFile
from django.db import models
import os
import zipfile
import StringIO
import codecs

class RequirementFeaturesAdminInline(admin.TabularInline):
    model = Requirement.feature.through
    verbose_name_plural = 'Related Features'
    verbose_name = 'Related Feature'
    #fk_name = 'scopeBacklog'
    extra = 0
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40,'class':'vLargeTextField',})},
    }

class RequirementAdmin(admin.ModelAdmin):
    form = RequirementForm
    fields = ['name','description','status_requirement_choices','requirement_type','priority', 'observations', ]
    inlines = [ RequirementFeaturesAdminInline ]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40,'class':'vLargeTextField',})},
    }
    list_display = ('name', 'requirement_type', 'priority')
    list_filter = ('feature',)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['has_report'] = True
        return super(RequirementAdmin, self).changelist_view(request, extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        opts = self.model._meta
        if not request.REQUEST.has_key("_change"):
            if request.REQUEST.has_key("_report"):
                body = Requirement.getReport()
                resp = HttpResponse(body, mimetype='application/pdf')
                resp['Content-Disposition'] = 'attachment; filename=requirements_report.pdf'
                return resp
            else:
                requirement = Requirement.objects.get(id=object_id)
                context = {
                    'requirement': requirement,
                    'title': _('Requiremen: %s') % force_unicode(requirement.name),
                    'opts': opts,
                    'object_id': object_id,
                    'is_popup': request.REQUEST.has_key('_popup'),
                    'app_label': opts.app_label,
                    }
                return render_to_response('admin/fur/requirement/view.html',
                                          context,
                                          context_instance=RequestContext(request))
        return super(RequirementAdmin, self).change_view(request, object_id,
            form_url, extra_context=None)


class RequirementTypeAdmin(admin.ModelAdmin):
    form = RequirementTypeForm
    def get_model_perms(self, request):
        return {}


admin.site.register(RequirementType, RequirementTypeAdmin)
admin.site.register(Requirement, RequirementAdmin)
