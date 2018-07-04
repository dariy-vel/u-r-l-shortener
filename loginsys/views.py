from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import auth


def register(request):
    args = {}
    args['form'] = RegistrationForm
    if request.POST:
        newuser_form = RegistrationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render(request, 'registration/register.html', args)