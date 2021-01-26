from django.contrib import admin
from .models import *

class ExaminationAdmin(admin.ModelAdmin):
    search_fields = ['ex_clt_nm']

class DiseaseAdmin(admin.ModelAdmin):
    search_fields = ['ds_nm_kr']
        
admin.site.register(Examination, ExaminationAdmin)
admin.site.register(Disease, DiseaseAdmin)

# class DiagnosisAdmin(admin.ModelAdmin):
#     search_fileds = ['ex_sn']

# admin.site.register(Diagnosis, DiagnosisAdmin)