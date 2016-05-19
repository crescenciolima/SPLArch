from SPLArch.architecture.forms import *
from SPLArch.architecture.models import *
from SPLArch.scoping.models import *
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from django.contrib.sites.models import Site
from django.http import HttpResponse
from django.utils.encoding import force_unicode
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _


class ApiAdmin(admin.ModelAdmin):
    form = ApiForm

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['has_report'] = True
        return super(ApiAdmin, self).changelist_view(request, extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        opts = self.model._meta
        if not request.REQUEST.has_key("_change"):
            if request.REQUEST.has_key("_report"):
                body = API.getReport()
                resp = HttpResponse(body, mimetype='application/pdf')
                resp['Content-Disposition'] = 'attachment; filename=api_report.pdf'
                return resp
            else:
                api = API.objects.get(id=object_id)
                context = {
                    'api': api,
                    'title': _('API: %s') % force_unicode(api.name),
                    'opts': opts,
                    'object_id': object_id,
                    'is_popup': request.REQUEST.has_key('_popup'),
                    'app_label': opts.app_label,
                }
                return render_to_response('admin/fur/api/view.html',
                                          context,
                                          context_instance=RequestContext(request))
        return super(ApiAdmin, self).change_view(request, object_id,
                                                 form_url, extra_context=None)


class ReferencesAdmin(admin.ModelAdmin):
    form = ReferencesForm

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['has_report'] = True
        return super(ReferencesAdmin, self).changelist_view(request, extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        opts = self.model._meta
        if not request.REQUEST.has_key("_change"):
            if request.REQUEST.has_key("_report"):
                body = References.getReport()
                resp = HttpResponse(body, mimetype='application/pdf')
                resp['Content-Disposition'] = 'attachment; filename=references_report.pdf'
                return resp
            else:
                references = References.objects.get(id=object_id)
                context = {
                    'references': references,
                    'title': _('References: %s') % force_unicode(references.title),
                    'opts': opts,
                    'object_id': object_id,
                    'is_popup': request.REQUEST.has_key('_popup'),
                    'app_label': opts.app_label,
                }
                return render_to_response('admin/fur/references/view.html',
                                          context,
                                          context_instance=RequestContext(request))
        return super(ReferencesAdmin, self).change_view(request, object_id,
                                                        form_url, extra_context=None)


class TechnologyAdmin(admin.ModelAdmin):
    form = TechnologyForm
    fields = ['api', 'description', ]
    filter_horizontal = ("api",)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['has_report'] = True
        return super(TechnologyAdmin, self).changelist_view(request, extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        opts = self.model._meta
        if not request.REQUEST.has_key("_change"):
            if request.REQUEST.has_key("_report"):
                body = Technology.getReport()
                resp = HttpResponse(body, mimetype='application/pdf')
                resp['Content-Disposition'] = 'attachment; filename=technology_report.pdf'
                return resp
            else:
                technology = Technology.objects.get(id=object_id)
                context = {
                    'technology': technology,
                    'title': _('Technology: %s') % force_unicode(technology.description),
                    'opts': opts,
                    'object_id': object_id,
                    'is_popup': request.REQUEST.has_key('_popup'),
                    'app_label': opts.app_label,
                }
                return render_to_response('admin/fur/technologies/view.html',
                                          context,
                                          context_instance=RequestContext(request))
        return super(TechnologyAdmin, self).change_view(request, object_id, form_url, extra_context=None)


class UseCaseMainStepsAdminInline(admin.TabularInline):
    model = MainSteps
    verbose_name_plural = 'Main Steps'
    verbose_name = 'Main Steps'
    # fk_name = 'scopeBacklog'
    extra = 0
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'vLargeTextField', })},
    }


class FeatureAdminInline(admin.TabularInline):
    model = Feature
    verbose_name_plural = 'Features'
    verbose_name = 'Feature'
    # fk_name = 'scopeBacklog'
    extra = 0
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'vLargeTextField', })},
    }


class UseCaseAlternativeStepsAdminInline(admin.TabularInline):
    model = AlternativeSteps
    verbose_name_plural = 'Secondary Steps'
    verbose_name = 'Secondary Steps'
    # fk_name = 'scopeBacklog'
    extra = 0
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'vLargeTextField', })},
    }


class UseCaseAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'f_requirements', 'owner', 'feature', 'precondition']
    inlines = [UseCaseMainStepsAdminInline, UseCaseAlternativeStepsAdminInline]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'vLargeTextField', })},
    }
    list_filter = ('feature',)
    filter_horizontal = ("feature", "owner", "f_requirements" )
    form = UseCaseForm

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['has_report'] = True
        return super(UseCaseAdmin, self).changelist_view(request, extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        opts = self.model._meta
        if not request.REQUEST.has_key("_change"):
            if request.REQUEST.has_key("_report"):
                body = UseCase.getReport()
                resp = HttpResponse(body, mimetype='application/pdf')
                resp['Content-Disposition'] = 'attachment; filename=usecase_report.pdf'
                return resp
            else:
                use_case = UseCase.objects.get(id=object_id)
                context = {
                    'use_case': use_case,
                    'title': _('Use Case: %s') % force_unicode(use_case.title),
                    'opts': opts,
                    'object_id': object_id,
                    'is_popup': request.REQUEST.has_key('_popup'),
                    'app_label': opts.app_label,
                }
                return render_to_response('admin/fur/usecase/view.html',
                                          context,
                                          context_instance=RequestContext(request))
        return super(UseCaseAdmin, self).change_view(request, object_id,
                                                     form_url, extra_context=None)


class ArchitectureAdmin(admin.ModelAdmin):
    form = ArchitectureForm

    def __unicode__(self):
        return '%s' % self.nome


class ScenariosAdmin(admin.ModelAdmin):
    form = ScenariosForm
    filter_horizontal = ("nf_requirement", "feature")


class DDSAdminInline(admin.TabularInline):
    model = DDSA.quality_attribute_priority.through

    verbose_name_plural = 'Quality Attribute Priority'
    verbose_name = 'Quality Attribute Priority'
    #fk_name = 'from_ddsa'
    extra = 0



class DSSAAdmin(admin.ModelAdmin):
    form = DSSAForm
    fields = ["name", "introduction", "references", "technology", "requirements",]
    filter_horizontal = ("references", "technology","requirements",)
    inlines = [DDSAdminInline]

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['has_report'] = True
        return super(DSSAAdmin, self).changelist_view(request, extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        opts = self.model._meta
        if not request.REQUEST.has_key("_change"):
            if request.REQUEST.has_key("_report"):
                body = DDSA.getReport()
                resp = HttpResponse(body, mimetype='application/pdf')
                resp['Content-Disposition'] = 'attachment; filename=dssa_report.pdf'
                return resp
            else:
                dssas = DDSA.objects.get(id=object_id)
                context = {
                    'dssas': dssas,
                    'title': _('DSSA: %s') % force_unicode(dssas.name),
                    'opts': opts,
                    'object_id': object_id,
                    'is_popup': request.REQUEST.has_key('_popup'),
                    'app_label': opts.app_label,
                }
                return render_to_response('admin/fur/dssa/view.html',
                                          context,
                                          context_instance=RequestContext(request))
        return super(DSSAAdmin, self).change_view(request, object_id, form_url, extra_context=None)

class QualityScenariosAdmin(admin.ModelAdmin):
    form = QualityScenariosForm
    filter_horizontal = ("nf_requirement",)

class QualityScenarioDocumentAdmin(admin.ModelAdmin):
     filter_horizontal = ("references", "quality_scenarios",)

     def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['has_report'] = True
        return super(QualityScenarioDocumentAdmin, self).changelist_view(request, extra_context=extra_context)

     def change_view(self, request, object_id, form_url='', extra_context=None):
        opts = self.model._meta
        if not request.REQUEST.has_key("_change"):
            if request.REQUEST.has_key("_report"):
                body = QualityScenarioDocument.getReport()
                resp = HttpResponse(body, mimetype='application/pdf')
                resp['Content-Disposition'] = 'attachment; filename=qualityscenariodocument_report.pdf'
                return resp
            else:
                qualityscenariodocument = QualityScenarioDocument.objects.get(id=object_id)
                context = {
                    'qualityscenariodocument': qualityscenariodocument,
                    'title': _('Quality Scenario Document: %s') % force_unicode(qualityscenariodocument.introduction),
                    'opts': opts,
                    'object_id': object_id,
                    'is_popup': request.REQUEST.has_key('_popup'),
                    'app_label': opts.app_label,
                }
                return render_to_response('admin/fur/qualityscenariodocument/view.html',
                                          context,
                                          context_instance=RequestContext(request))
        return super(QualityScenarioDocumentAdmin, self).change_view(request, object_id, form_url, extra_context=None)

admin.site.unregister(Site)
admin.site.register(UseCase, UseCaseAdmin)
admin.site.register(References, ReferencesAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(API, ApiAdmin)
admin.site.register(Architecture)
admin.site.register(DDSA, DSSAAdmin)
admin.site.register(QualityScenarios, QualityScenariosAdmin)
admin.site.register(Scenarios, ScenariosAdmin)
admin.site.unregister(Architecture)
admin.site.register(QualityScenarioDocument, QualityScenarioDocumentAdmin)