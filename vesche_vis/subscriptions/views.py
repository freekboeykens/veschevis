from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .models import Cooperant, CollectionPoint, WeeklySubscription
from .forms import CooperantForm
from .tables import CooperantTable, CollectionPointTable
from reportlab.pdfgen import canvas

# =============================================================================
# COOPERANT CREATE VIEW
# =============================================================================
class CooperantCreateView(CreateView):
    model = Cooperant
    form_class = CooperantForm
    template_name = 'subscriptions/cooperant_form.html'
    success_url = '/thanks/'  # TODO

    # TODO: use stand-alone function to create unique code?

# =============================================================================
# COOPERANT DETAIL VIEW
# =============================================================================
class CooperantDetailView(DetailView):
    model = Cooperant
    context_object_name = 'cooperant'
    template_name = 'subscriptions/cooperant_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CooperantDetailView, self).get_context_data(**kwargs)
        subscription_set = self.object.subscription_set.all()
        table = CooperantTable(subscription_set)
        context['table'] = table
        return context

# =============================================================================
# COLLECTION POINT DETAIL VIEW
# =============================================================================
class CollectionPointDetailView(DetailView):
    model = CollectionPoint
    context_object_name = 'collection_point'
    template_name = 'subscriptions/collection_point_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CollectionPointDetailView, self).get_context_data(**kwargs)
        subscription_set = self.object.subscription_set.all()
        table = CollectionPointTable(subscription_set)
        context['table'] = table
        return context

# =============================================================================
# TEST PDF: HELLO WORLD
# =============================================================================
def test_pdf_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
