# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'medizen'

# API
# examination_list = views.ExaminationViewSet.as_view({
#     'post': 'create',
#     'get': 'list',
# })
# examination_detail = views.ExaminationViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })

# disease_list = views.DiseaseViewSet.as_view({
#     'post': 'create',
#     'get': 'list',
# })
# disease_detail = views.DiseaseViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })

# diagnosis_list = views.DiagnosisViewSet.as_view({
#     'post': 'create',
#     'get': 'list',
# })
# diagnosis_detail = views.DiagnosisViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })

 # url
urlpatterns = [
    path('', views.search, name = 'search'), # medizen.html
    path('<int:examination_ex_sn>', views.exam, name = 'exam'), # examination.html

    # API
    # path('auth', include('rest_framework.urls', namespace = 'rest_framework')),
    # path('examination', examination_list, name = 'examination_list'),
    # path('examination/<int:pk>', examination_detail, name = 'examination_detail'),
    # path('disease', disease_list, name = 'disease_list'),
    # path('disease/<str:pk>', disease_detail, name = 'disease_detail'),
    # path('diagnosis', diagnosis_list, name = 'diagnosis_list'),
    # path('diagnosis/<pk>', diagnosis_detail, name = 'diagnosis_detail'),
]

# API
# from rest_framework import routers
# from medizen.views import *

# router = routers.DefaultRouter()
# router.register(r'examination', ExaminationViewSet)
# router.register(r'disease', DiseaseViewSet)
# router.register(r'diagnosis', DiagnosisViewSet)

# urlpatterns = [
#     path('', views.search, name = 'search'),
#     path('<int:examination_ex_sn>/', views.exam, name = 'exam'),
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)