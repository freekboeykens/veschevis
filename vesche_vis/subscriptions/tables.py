import django_tables2 as tables
from .models import WeeklySubscription

# =============================================================================
# COOPERANT TABLE
# =============================================================================
class CooperantTable(tables.Table):
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

# =============================================================================
# COLLECTION POINT TABLE
# =============================================================================
class CollectionPointTable(tables.Table):
    class Meta:
        model = WeeklySubscription
        attrs = { "class": "paleblue" }
        fields = (
            'cooperant',
            'subscription_type',
            'date',
            'amount',
            'is_paid',
         )
