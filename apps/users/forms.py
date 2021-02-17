from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm

input_form_appearance = 'block mb-8 mt-2 shadow appearance-none border rounded py-2 px-3 text-grey-darker'


class CustomUserCreation(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['username'].widget.attrs.update({'class': input_form_appearance})
        self.fields['password1'].widget.attrs.update({'class': input_form_appearance})
        self.fields['password2'].widget.attrs.update({'class': input_form_appearance})

    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': input_form_appearance}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': input_form_appearance})
        self.fields['password'].widget.attrs.update({'class': input_form_appearance})
        self.label_suffix = ''


class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': input_form_appearance})


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({'class': input_form_appearance})
        self.fields['new_password2'].widget.attrs.update({'class': input_form_appearance})
