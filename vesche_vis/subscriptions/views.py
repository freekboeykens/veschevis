from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .models import Cooperant
from .forms import CooperantForm
from .tables import SubscriptionTable

class CooperantCreateView(CreateView):
    model = Cooperant
    form_class = CooperantForm
    template_name = 'subscriptions/cooperant_form.html'
    success_url = '/thanks/'  # TODO

    # TODO: use stand-alone function to create unique code?

class CooperantDetailView(DetailView):
    model = Cooperant
    template_name = 'subscriptions/cooperant_detail.html'

class CooperantSubscriptionsView(DetailView):
    model = Cooperant
    template_name = 'subscriptions/cooperant_subscriptions.html'

#    def get(self, request):
#        table = SubscriptionTable(cooperant.subscription_set.all())
#        return HttpResponse(table)
