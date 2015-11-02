from django.conf.urls import url
from . import views

urlpatterns = [
    # e.g. /subscriptions/add_cooperant/
    url(
        r'^add_cooperant/$',
        views.CooperantCreateView.as_view(),
        name='add_cooperant',
    ),
    # e.g. /subscriptions/cooperant/1/
    url(
        r'^cooperant/(?P<pk>[0-9]+)/$',
        views.CooperantDetailView.as_view(),
        name='cooperant_detail',
    ),
]
