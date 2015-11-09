import django_tables2 as tables
from .models import Cooperant

class CooperantTable(tables.Table):
    class Meta:
        model = Cooperant
        attrs = { "class": "paleblue" }
