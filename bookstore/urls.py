from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('index/'   , views.index , name ='index'),
    path('aggregate_fuction/'   , views.aggregate_fuction , name ='aggregate_fuction'),
    path('aggregate_Multi/'   , views.aggregate_Multi , name ='aggregate_Multi'),
    path('annotate_function/'   , views.annotate_function , name ='annotate_function'),
]
