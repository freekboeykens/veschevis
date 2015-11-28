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
        p = canvas.Canvas(buffer, pagesize = A4)
        width, self.height = A4
        styles = getSampleStyleSheet()

        # WRite collection point name
        collectionpoint = """ <font size="9">
        Afhaalpunt: %s<br/>
        </font>
        """ % (self.collection_point.name)
        par = Paragraph(collectionpoint, styles["Normal"])
        par.wrapOn(p, width, self.height)
        par.drawOn(p, *self.coord(18, 40, mm))

        # write data
        data = []
        data.append(["Coöperant", "Pakket", "Aantal", "Handtekening"])
        for subscription in self.collection_point.subscription_set.all():
            row = []
            row.append(subscription.cooperant)
            row.append(subscription.subscription_type)
            row.append(subscription.amount)
            row.append("")
            data.append(row)
        t = Table(data, 1.5 * inch)
        t.setStyle(TableStyle([
            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
            ('BOX', (0,0), (-1,-1), 0.25, colors.black)
        ]))
        t.wrapOn(p, width, self.height)
        t.drawOn(p, *self.coord(18, 85, mm))

        # Close the PDF object cleanly.
        p.showPage()
        p.save()

        # Get the value of the BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()

        return pdf

    def coord(self, x, y, unit=1):
        """
        # http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
        Helper class to help position flowables in Canvas objects
        """
        x, y = x * unit, self.height -  y * unit
        return x, y
