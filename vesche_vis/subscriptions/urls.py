from django.conf.urls import url
from . import views

urlpatterns = [
    #e.g. /subscriptions/add_cooperant
    url(
        r'^add_cooperant/$'
        views.CooperantCreateView.as_view(),
        name='add_cooperant',
    ),
]
