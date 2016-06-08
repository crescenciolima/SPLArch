from django.contrib import admin
from SPLArch.decisions.models import Decision, Pattern, TypeDecision, TypePattern

class TypePatternAdmin(admin.ModelAdmin):
    pass

class TypeDecisionAdmin(admin.ModelAdmin):
    pass

class PatternAdmin(admin.ModelAdmin):
     filter_horizontal = ('padroesRelacionados',)

class DecisionAdmin(admin.ModelAdmin):
    filter_horizontal = ('decisaoRelacionada', 'padraoUtilizado')

admin.site.register(TypePattern)
admin.site.register(TypeDecision)
admin.site.register(Pattern, PatternAdmin)
admin.site.register(Decision, DecisionAdmin)