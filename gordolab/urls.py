"""Defines URL patterns for gordos."""

from django.urls import path
from . import views


app_name = 'gordolab'
urlpatterns =[
    #Home page
    path('', views.index, name='index'),
    #Page that show project gordofut
    path('gordofut/', views.gordofut, name= 'gordofut'),
    #Page that show about us
    path('quienessomos/', views.quienessomos, name= 'quienessomos'),

    

        
]