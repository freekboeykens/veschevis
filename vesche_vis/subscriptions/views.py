from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Cooperant
from .forms import CooperantForm

class CooperantCreateView(CreateView):
    model = Cooperant
    form_class = CooperantForm
    template_name = 'subscriptions/cooperant_form.html'
    success_url = '/thanks/'  # TODO

    # TODO: use stand-alone function to create unique code?
