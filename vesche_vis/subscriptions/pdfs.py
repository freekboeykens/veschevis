from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle
from .models import Cooperant, CollectionPoint, WeeklySubscription

# =============================================================================
# COLLECTION POINT PDF
# =============================================================================
class CollectionPointPDF:

    def __init__(self, collection_point):
        self.collection_point = collection_point

    def create_pdf(self):
        buffer = BytesIO()

        # Create the PDF object, using the BytesIO object as its "file."
        p = canvas.Canvas(buffer, pagesize=A4)

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.

        p.drawString(100, 100, self.collection_point.name)

        # Close the PDF object cleanly.
        p.showPage()
        p.save()

        # Get the value of the BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()

        return pdf
