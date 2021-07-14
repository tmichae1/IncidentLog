from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(StaffRole)
admin.site.register(IncidentLocation)
admin.site.register(IncidentType)
admin.site.register(Report)
admin.site.register(AppSetting)

