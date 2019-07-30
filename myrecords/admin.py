from django.contrib import admin
from myrecords.models import *
# Register your models here.
admin.site.register(Records)
admin.site.register(State)
admin.site.register(District)
admin.site.register(InstitutionType)
admin.site.register(InstitutionName)
admin.site.register(CaseType)