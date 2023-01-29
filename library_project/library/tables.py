import django_tables2 as tables
from django.utils.html import format_html
from .models import Book, User

class ImageColumn(tables.Column):
    def render(self, value):
        return format_html('<img src="{}" />', value)

class AuthorColumn(tables.Column):
    def render(self, value):
        res = ''
        for author in value:
            res += str(author[0]) + ','
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
    thumbnail = ImageColumn('Thumbnail')
    authors = AuthorColumn('Authors')
    class Meta:
        model = Book
        attrs = {"class": "table",
                 'thead': {
                     'class': 'thead-dark'
                 }}
        fields = ("thumbnail", "title", "authors")

class UserTable(tables.Table):
    class Meta:
        model = User
        attrs = {"class": "table",
                 'thead': {
                     'class': 'thead-dark'
                 }}
        fields = ("name", "card_id")