from django_tables2 import A, Table, tables

from .models import Deck


class DeckTable(Table):
    title = tables.columns.Column(linkify=("preview", {"pk": A("pk")}))
    actions = tables.columns.TemplateColumn(template_name="deck/actions.html")

    class Meta:
        model = Deck
        fields = ("title", "created", "modified", "actions")
        attrs = {"class": "table table-striped"}
