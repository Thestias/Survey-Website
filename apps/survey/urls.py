from django.urls import path
from . import views

urlpatterns = [
    # BELOW - PATHS TO RENDERING STUFF FOR THE USER
    # This one displays survey title, description and should have administrative tools for the OWNERS
    path('<survey_id>/', views.survey, name='survey'),

    # Displays the questions and their options
    #path('<survey_id>', views.start_survey, name='start_survey'),
    #
    path('edit/<survey_id>/', views.edit_questions, name='edit_questions'),

    # BELOW - PATHS FOR AJAX REQUESTS
    # This one recieves AJAX POST requests to add/edit surveys
    path('edit/submit/<survey_id>/', views.ajax_edit_questions, name='ajax_edit_questions'),

    # When a User SUBMITS its answers
    #path('<survey_id>/submit', views.submit_survey, name='submit_survey')
]
