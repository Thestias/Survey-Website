from django.urls import path
from . import views

urlpatterns = [
    path('create_survey/', views.create_survey, name='create_survey'),
]
