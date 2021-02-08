from django.shortcuts import render, redirect
from .forms import CustomUserCreation
from ..survey.models import Survey, Submission
# Create your views here.


def register(request):
    if request.method == 'POST':
        register_form = CustomUserCreation(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
    else:
        register_form = CustomUserCreation()
    return render(request, 'users/register.html', context={'form': register_form})


def profile(request):
    user_surveys = Survey.objects.filter(author=request.user.id)

    return render(request, 'users/profile.html', context={'user_surveys': user_surveys})
