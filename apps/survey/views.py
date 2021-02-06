from .forms import QuestionFormSet, OptionFormSet
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Survey, Option, Question
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


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


@login_required(login_url='/login')
def add_survey(request, survey_id):
    survey_instance = get_object_or_404(Survey, id=survey_id)

    if survey_instance.author.id != request.user.id:  # Checking ownership
        return JsonResponse({'Error': 'You are not the owner of this survey!'})

    if request.method == 'POST':
        survey_instance = get_object_or_404(Survey, id=survey_id)
        question_formset = QuestionFormSet(request.POST, request.FILES, instance=survey_instance)

        try:
            if question_formset.is_valid():
                question_formset.save()
                return JsonResponse({'Success': 'Survey Created Succesfully!'})
        except Exception as e:
            print(e)
            return JsonResponse({'Error': e})
