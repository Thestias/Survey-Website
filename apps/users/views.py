from django.shortcuts import render, redirect
from .forms import CustomUserCreation
# Create your views here.


def register(request):
    if request.method == 'POST':
        register_form = CustomUserCreation(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
    else:
        register_form = CustomUserCreation(label_suffix='')
    return render(request, 'users/register.html', context={'form': register_form})
