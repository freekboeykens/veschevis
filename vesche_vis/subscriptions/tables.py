import django_tables2 as tables
from .models import WeeklySubscription

class SubscriptionTable(tables.Table):
    class Meta:
        model = WeeklySubscription
        attrs = { "class": "paleblue" }
