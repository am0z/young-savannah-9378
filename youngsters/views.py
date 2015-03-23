from django.core.urlresolvers import reverse
from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import FormView
from .forms import *


class LoginFormView(FormView):
    form_class = YoungstersLoginForm
    template_name = 'youngsters/login_form.html'

    def get_success_url(self):
        return reverse('youngsters:profile')

    def form_valid(self, form):
        user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password'])
        login(self.request, user)
        return super(LoginFormView, self).form_valid(form)
