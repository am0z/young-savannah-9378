from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import FormView
from .forms import *


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact/form.html'

    def get_success_url(self):
        return reverse('contact:thanks')

    def form_valid(self, form):
        send_mail('New contact', form.cleaned_data['content'],
            settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
        return super(ContactFormView, self).form_valid(form)
