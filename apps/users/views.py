from django.shortcuts import render, redirect
from .forms import CustomUserCreation

# Create your views here.


def register(request):
    if request.method == 'POST':
        register_form = CustomUserCreation(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('home')
    else:
        register_form = CustomUserCreation()

    return render(request, 'users/register_login.html', context={'form': register_form, 'action': 'Register'})
