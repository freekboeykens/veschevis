import django_tables2 as tables
from .models import WeeklySubscription

class SubscriptionTable(tables.Table):
    class Meta:
        model = WeeklySubscription
        attrs = { "class": "paleblue" }
        fields = (
            'collection_point',
            'subscription_type',
            'date',
            'amount',
            'is_paid',
         )
