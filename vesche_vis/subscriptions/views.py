from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .models import Cooperant, CollectionPoint, WeeklySubscription
from .forms import CooperantForm

class CooperantCreateView(CreateView):
    model = Cooperant
    form_class = CooperantForm
    template_name = 'subscriptions/cooperant_form.html'
    success_url = '/thanks/'  # TODO

    # TODO: use stand-alone function to create unique code?

class CooperantDetailView(DetailView):
    model = Cooperant
    context_object_name = 'cooperant'
    template_name = 'subscriptions/cooperant_detail.html'

class CollectionPointDetailView(DetailView):
    model = CollectionPoint
    context_object_name = 'collection_point'
    template_name = 'subscriptions/collection_point_detail.html'
