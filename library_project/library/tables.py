import django_tables2 as tables
from django.utils.html import format_html
from .models import Book

class ImageColumn(tables.Column):
    def render(self, value):
        return format_html('<img src="{}" />', value)

class AuthorColumn(tables.Column):
    def render(self, value):
        res = ''
        for author in value:
            res += res + str(author) + ','
        return res[:-1]

class BookTable(tables.Table):
    thumbnail = ImageColumn('Thumbnail')
    authors = AuthorColumn('Authors')
    class Meta:
        model = Book
        attrs = {"class": "table",
                 'thead': {
                     'class': 'thead-dark'
                 }}
        fields = ("thumbnail", "title", "authors", "quantity")

class UserBookTable(tables.Table):
    thumbnail = ImageColumn('Thumbernail')
    authors = AuthorColumn('Authors')
    class Meta:
        model = Book
        attrs = {"class": "table",
                 'thead': {
                     'class': 'thead-dark'
                 }}
        fields = ("thumbnail", "title", "authors")
