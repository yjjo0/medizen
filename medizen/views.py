from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from  .models import *

 # medizen.html
def search(request):
    template_name = 'medizen/medizen.html'
    examination = Examination.objects.all() # get all examination
    cn = request.GET.get('cn', '') # get clt_nm from medizen page
    cd = request.GET.get('cd', '') # get cd from medizen page
    on = request.GET.get('on', '') # get obj_nm from medizen page
        
    if cn and cd and on:
        examination_cn = examination.filter(ex_clt_nm = cn)          # examination filtered by cn
        examination_cncd = examination_cn.filter(ex_cd = cd)         # examination filtered by cd
        examination_cncdon = examination_cncd.filter(ex_obj_nm = on) # examination filtered by on
    else:
        examination_cncdon = ''
    
     # final data
    context = {
        'examination' : examination_cncdon
        }
    
    return render(request, template_name, context)

 # examination.html
def exam(request, examination_ex_sn): # get exmaination_ex_sn from medizen page
    template_name = 'medizen/examination.html'
    examination = Examination.objects.get(ex_sn = examination_ex_sn) # examination filtered by ex_sn
    diagnosis = Diagnosis.objects.filter(ex_sn = examination_ex_sn)  # diagnosis filtered by ex_sn
    disease = Disease.objects.all()                                  # get all disease
    
     # final data
    context = {
        'examination' : examination,
        'diagnosis' : diagnosis,
        'disease' : disease,
        }
    
    return render(request, template_name, context)

# API
# from rest_framework import viewsets
# from rest_framework import permissions
# from .serializers import *

# class ExaminationViewSet(viewsets.ModelViewSet):
#     queryset = Examination.objects.all()
#     serializer_class = ExaminationSerializer

#     def perform_create(self, serializer):
#         serializer.save()

# class DiseaseViewSet(viewsets.ModelViewSet):
#     queryset = Disease.objects.all()
#     serializer_class = DiseaseSerializer

#     def perform_create(self, serializer):
#         serializer.save()

# class DiagnosisViewSet(viewsets.ModelViewSet):
#     queryset = Diagnosis.objects.all()
#     serializer_class = DiagnosisSerializer

#     def perform_create(self, serializer):
#         serializer.save()