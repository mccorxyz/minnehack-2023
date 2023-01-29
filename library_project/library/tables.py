import django_tables2 as tables
from .models import Book

class BookTable(tables.Table):
    title = tables.Column()
    class Meta:
        model = Book