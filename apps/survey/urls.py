from django.urls import path
from . import views

urlpatterns = [
    # BELOW - PATHS TO RENDERING STUFF FOR THE USER
    # This one displays survey title, description and should have administrative tools for the OWNERS
    #path('<survey_id>', views.survey, name='survey'),

    # Displays the questions and their options
    #path('<survey_id>', views.start_survey, name='start_survey'),
    #
    path('edit/<survey_id>', views.create_survey, name='create_survey'),

    # BELOW - PATHS FOR AJAX REQUESTS
    # This one recieves AJAX POST requests to add/edit surveys
    path('edit/submit/<survey_id>', views.add_survey, name='add_survey'),

    # When a User SUBMITS its answers
    #path('<survey_id>/submit', views.submit_survey, name='submit_survey')
]
