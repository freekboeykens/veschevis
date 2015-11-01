from django.shortcuts import render
from django.views.generic.edit import CreateView

class CooperantCreateView(CreateView):
    model = Cooperant
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
