from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Cooperant

class CooperantCreateView(CreateView):
    model = Cooperant
    template_name = 'subscriptions/cooperant_form.html'
    fields = [
        'first_name',
        'last_name',
        'phone',
        'email',
        'street_and_number',
        'zip_code',
        'city',
    ]

    # TODO: use stand-alone function to create unique code?
