from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('index/'            , views.index             , name ='index'),
    path('filter/'           , views.filter            , name ='filter'),
    path('complex_filter/'   , views.complex_filter    , name ='complex_filter'),
    path('MultiFilter/'      , views.MultiFilter       , name ='MultiFilter'),
    path('MultiQueryFilter/' , views.MultiQueryFilter  , name ='MultiQueryFilter'),
    path('Not_Q_exclude/'    , views.Not_Q_exclude     , name ='Not_Q_exclude'),
    path('valuesfunction/'   , views.valuesfunction    , name ='valuesfunction'),
    path('values_list_function/'   , views.values_list_function    , name ='values_list_function'),
    path('distinct_function/'   , views.distinct_function    , name ='distinct_function'),
    path('orderby_function/'   , views.orderby_function    , name ='orderby_function'),
    path('related_function/'   , views.related_function    , name ='related_function'),
]
