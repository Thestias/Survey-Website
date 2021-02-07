from .forms import QuestionFormSet, OptionFormSet
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Survey, Option, Question
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages

# Create your views here.


@require_http_methods(['GET'])
@login_required(login_url='/login')
def create_survey(request, survey_id):
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
def add_survey(request, survey_id):
    survey_instance = get_object_or_404(Survey, id=survey_id)

    if survey_instance.author.id != request.user.id:  # Checking ownership
        return JsonResponse({'Error': 'You are not the owner of this survey!'})

    question_formset = QuestionFormSet(request.POST, instance=survey_instance)
    if question_formset.is_valid():
        question_formset.save()
        return JsonResponse({'Success': 'Survey updated/created succesfully'})
    else:
        return JsonResponse({'Error': 'Error while creating survey', 'Errors': question_formset.errors})
