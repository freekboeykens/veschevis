from django.shortcuts import render
from django.views.generic.edit import CreateView

class CooperantCreateView(CreateView):
    model = Cooperant
    template_name = 'subscriptions/cooperant_form.html'
    fields = [
        'first_name',
        'last_name',
        'phone',
        'email',
        'street',
        'number',
        'mailbox',
        'zip_code',
        'city',
    ]

    # TODO: use stand-alone function to create unique code?
