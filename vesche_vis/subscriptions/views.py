from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .models import Cooperant, CollectionPoint, WeeklySubscription
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
    context_object_name = 'cooperant'
    template_name = 'subscriptions/cooperant_detail.html'

class CooperantSubscriptionsView(DetailView):
    model = Cooperant
    context_object_name = 'cooperant'
    template_name = 'subscriptions/cooperant_subscriptions.html'

    def get_context_data(self, **kwargs):
        context = super(CooperantSubscriptionsView, self).get_context_data(**kwargs)
        subscription_set = self.object.subscription_set.all()
        table = CooperantTable(subscription_set)
        context['table'] = table
        return context

#    def get(self, request):
#        table = SubscriptionTable(cooperant.subscription_set.all())
#        return HttpResponse(table)
class CollectionPointDetailView(DetailView):
    model = CollectionPoint
    context_object_name = 'collection_point'
    template_name = 'subscriptions/collection_point_detail.html'
