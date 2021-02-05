from django.urls import path
from . import views

urlpatterns = [
    path('create_survey/<survey_id>', views.create_survey, name='create_survey'),
    path('create_survey/add/<survey_id>', views.add_survey, name='add_survey'),
]
