from django.contrib import admin
from .models import Cooperant
from .models import CollectionPoint
from .models import SubscriptionType
from .models import WeeklySubscription

# =============================================================================
# SUBSCRIPTION INLINE
# =============================================================================
class SubscriptionInline(admin.TabularInline):
    model = WeeklySubscription

# =============================================================================
# COOPERANT ADMIN
# =============================================================================
class CooperantAdmin(admin.ModelAdmin):
    inlines = [SubscriptionInline]

# =============================================================================
# REGISTERED MODELS
# =============================================================================
admin.site.register(Cooperant, CooperantAdmin)
admin.site.register(CollectionPoint)
admin.site.register(SubscriptionType)
