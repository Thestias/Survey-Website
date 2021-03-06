from django.urls import path
from . import views

urlpatterns = [
    # BELOW - PATHS TO RENDERING STUFF FOR THE USER
    # This one displays survey title, description and should have administrative tools for the OWNERS
    path('<survey_id>/', views.survey, name='survey'),

    # Displays the questions and their options
    path('<survey_id>/start', views.start_survey, name='start_survey'),
    #
    path('<survey_id>/edit/', views.edit_questions, name='edit_questions'),

    # BELOW - PATHS FOR AJAX REQUESTS
    # This one recieves AJAX POST requests to add/edit surveys
    path('<survey_id>/edit/submit/', views.ajax_edit_questions, name='ajax_edit_questions'),

    # The stats of a survey
    path('<survey_id>/stats/', views.survey_stats, name='survey_stats')
]
