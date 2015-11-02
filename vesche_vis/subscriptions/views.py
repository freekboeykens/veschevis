from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import CooperantForm

class CooperantFormView(FormView):
    template_name = 'subscriptions/cooperant_form.html'
    form_class = CooperantForm
    success_url = '/thanks/'  # TODO

    # TODO: use stand-alone function to create unique code?
