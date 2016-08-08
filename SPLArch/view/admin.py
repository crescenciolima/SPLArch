from django.contrib import admin
from SPLArch.component.models import *
from .models import *

admin.site.register(View)
admin.site.register(StructuralView)
admin.site.register(ViewPoint)
admin.site.register(BehaviorView)
admin.site.register(VariabilityGuidelines)