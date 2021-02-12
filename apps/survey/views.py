from .forms import QuestionFormSet, OptionFormSet, SurveyForm, QuestionAnswerFormSet, AnswerForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Survey, Option, Question, Answer, Submission
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages

# Create your views here.


@require_http_methods(['GET'])
@login_required
def edit_questions(request, survey_id):
    '''
    This function allows the OWNER of a Survey to edit all of it's questions
    and options.
    '''
    survey_instance = get_object_or_404(Survey, id=survey_id)

    if survey_instance.author.id != request.user.id:  # Checking ownership
        messages.error(request, 'You are not the owner of this survey!')
        return redirect('register')

    question_formset = QuestionFormSet(instance=survey_instance, participate=False)

    return render(
        request, 'survey/edit_questions.html',
        context={'form': question_formset, 'survey_id': survey_instance.id})


@require_http_methods(['POST'])
@login_required
def ajax_edit_questions(request, survey_id):
    '''
    This function recieves the data from edit_questions() trought
    a AJAX POST request
    '''
    try:
        survey_instance = Survey.objects.get(pk=survey_id)
    except Survey.DoesNotExist:
        return JsonResponse({'Error': 'This Survey doesnt exist!'}, status=404)

    if survey_instance.author.id != request.user.id:  # Checking ownership
        return JsonResponse({'Error': 'You are not the owner of this survey!'})

    question_formset = QuestionFormSet(request.POST, instance=survey_instance, participate=False)

    if question_formset.is_valid():
        question_formset.save()
        return JsonResponse({'Success': 'Survey updated/created succesfully'})
    else:
        return JsonResponse({'Error': 'Error while creating survey', 'Errors': question_formset.errors})


@require_http_methods(['POST', 'GET'])
def survey(request, survey_id):
    '''
    This function displays the title and description of a survey to a user,
    to it's owner, also shows management tools
    '''
    survey = get_object_or_404(Survey, id=survey_id)
    context = {'survey': survey}

    if request.method == 'POST':
        if 'delete' in request.POST:
            survey.delete()
            messages.info(request, 'Survey deleted!')
            return redirect('profile')
        else:
            survey_edit_form = SurveyForm(request.POST, instance=survey)
            if survey_edit_form.is_valid():
                messages.success(request, 'Survey updated!')
                survey_edit_form.save()
            else:
                messages.error(request, 'Invalid form!')
    else:
        if request.user.id == survey.author.id:
            survey_edit_form = SurveyForm(instance=survey)
            context['survey_edit_form'] = survey_edit_form

    return render(request, template_name='survey/survey.html', context=context)


def start_survey(request, survey_id):
    '''
    This function renders the survey for the users to participate.
    What is does is:
        Renders the Survey and it's options
        Gets the POST data, creates a Submission instance and a AnswerForm(for each question) and saves it.

    In the template for this view you may see that the value of the radio input is shown as field.data.value.value
    for some reason Django wouldnt let me access it as field.value so i had to do that.
    '''
    context = {}
    survey = get_object_or_404(Survey, id=survey_id)
    question_answering = QuestionAnswerFormSet(instance=survey, participate=True)

    if request.method == 'POST':
        submission = Submission.objects.create(survey=survey)
        for k, v in request.POST.items():
            if k.startswith('option'):

                option_id = request.POST[k]  # option-NUMBER   is the k
                question_id = k.split('-')[-1]  # option-NUMBER  Number is the question ID

                answer_data = {'submission': submission.id,
                               'option': Option.objects.get(id=option_id),
                               'question': Question.objects.get(id=question_id)}
                form_ans = AnswerForm(answer_data)
                if form_ans.is_valid():
                    form_ans.save()
                else:
                    print(form_ans.errors)
                    messages.error(request, 'We had a unexpected error')
        else:
            messages.success(request, 'Survey submitted')
            return redirect('survey', survey_id=survey_id)

    context['form'] = question_answering
    return render(request, template_name='survey/survey_start.html',
                  context=context)
