from django.contrib import admin
from SPLArch.component.models import *
from .models import *
from .forms import *

admin.site.register(View)
admin.site.register(StructuralView)
admin.site.register(ViewPoint)
admin.site.register(BehaviorView)
admin.site.register(VariabilityGuidelines)

class QualityTypeAdmin(admin.ModelAdmin):
    form = QualityForm
    def get_model_perms(self, request):
        return {}


admin.site.register(Quality, QualityTypeAdmin)