from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('index/'          , views.index           , name ='index'),
    path('filter/'         , views.filter          , name ='filter'),
    path('complex_filter/' , views.complex_filter  , name ='complex_filter'),
    path('MultiFilter/'    , views.MultiFilter     , name ='MultiFilter'),
    path('MultiQueryFilter/'    , views.MultiQueryFilter     , name ='MultiQueryFilter'),
]
