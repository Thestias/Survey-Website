from .forms import QuestionFormSet, OptionFormSet, SurveyForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Survey, Option, Question
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages

# Create your views here.


@require_http_methods(['GET'])
@login_required(login_url='/login')
def edit_questions(request, survey_id):
    '''
    This function allows the OWNER of a Survey to edit all of it's questions
    and options.
    '''
    survey_instance = get_object_or_404(Survey, id=survey_id)

    if survey_instance.author.id != request.user.id:  # Checking ownership
        messages.error(request, 'You are not the owner of this survey!')
        return redirect('register')

    question_formset = QuestionFormSet(instance=survey_instance)

    return render(
        request, 'survey/update_survey.html',
        context={'question_formset': question_formset, 'survey_id': survey_instance.id})


@require_http_methods(['POST'])
@login_required(login_url='/login')
def ajax_edit_questions(request, survey_id):
    '''
    This function recieves the data from edit_questions() trought
    a AJAX POST request
    '''
    survey_instance = get_object_or_404(Survey, id=survey_id)

    if survey_instance.author.id != request.user.id:  # Checking ownership
        return JsonResponse({'Error': 'You are not the owner of this survey!'})

    question_formset = QuestionFormSet(request.POST, instance=survey_instance)
    if question_formset.is_valid():
        question_formset.save()
        return JsonResponse({'Success': 'Survey updated/created succesfully'})
    else:
        return JsonResponse({'Error': 'Error while creating survey', 'Errors': question_formset.errors})


def survey(request, survey_id):
    '''
    This function displays the title and description of a survey to a user,
    to it's owner, also shows management tools
    '''
    survey = get_object_or_404(Survey, id=survey_id)
    if request.user.id == survey.author.id:
        question_edit_form = SurveyForm(instance=survey)

    if request.method == 'POST':
        if 'delete' in request.POST:
            survey.delete()
            messages.info(request, 'Survey deleted!')
            return redirect('profile')
        else:
            survey_data = SurveyForm(request.POST, instance=survey)
            if survey_data.is_valid():
                messages.success(request, 'Survey updated!')
                survey_data.save()
            else:
                messages.error(request, 'Invalid form!')

    return render(request, template_name='survey/survey.html',
                  context={'survey': survey, 'question_edit_form': question_edit_form or None})
