from django.shortcuts import render, redirect
from .forms import CustomUserCreation
from ..survey.models import Survey, Submission
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        register_form = CustomUserCreation(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
    else:
        register_form = CustomUserCreation()
    return render(request, 'users/register.html', context={'form': register_form})


@login_required
def profile(request):
    user_surveys = Survey.objects.filter(author=request.user.id)
    if request.method == 'POST':
        if 'add-survey' in request.POST:
            try:
                survey = Survey(author=request.user)
            except Exception as e:
                messages.error(request, e)
            else:
                survey.save()
                messages.success(request, 'Survey Created!')
        elif 'delete-survey' in request.POST:
            try:
                survey = Survey(request.POST.get('delete-survey')).delete()
            except Exception as e:
                messages.error(request, e)
            else:
                messages.success(request, 'Survey sucessfully deleted')

    return render(request, 'users/profile.html', context={'user_surveys': user_surveys})
