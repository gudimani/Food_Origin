# products/tables.py
import django_tables2 as tables
from .models import Egg

class EggTable(tables.Table):
    class Meta:
        model = Egg
        template_name = "tables/bootstrap_htmx.html"
        fields = ('eggtype','color', 'size', 'weight')