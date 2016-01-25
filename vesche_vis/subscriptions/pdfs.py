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
        """
        Creates the PDF for a collection point.
        """

        buffer = BytesIO()

        # Create the PDF object, using the BytesIO object as its "file"
        p = canvas.Canvas(buffer, pagesize = A4)
        self.width, self.height = A4
        self.styles = getSampleStyleSheet()

        # Write collection point name
        info = self.__collection_point_info()
        info.wrapOn(p, self.width, self.height)
        info.drawOn(p, *self.__coord(18, 40, mm))

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
        t.wrapOn(p, self.width, self.height)
        t.drawOn(p, *self.__coord(18, 85, mm))

        # Close the PDF object cleanly.
        p.showPage()
        p.save()

        # Get the value of the BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()

        return pdf

    def __collection_point_info(self):
        """
        Writes collection point info to the PDF.
        """

        info = """
        <font size="9">
        Afhaalpunt: %s
        <br/> </font>
        """ % (self.collection_point.name)
        par = Paragraph(info, self.styles["Normal"])

        return par



    def __coord(self, x, y, unit=1):
        """
        Helps positioning flowables in Canvas objects.
        http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
        """
        x, y = x * unit, self.height -  y * unit
        return x, y
