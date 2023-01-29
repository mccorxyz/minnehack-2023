from django.forms import ModelForm, DateInput, TextInput
from django import forms
from .models import Book


class ManualAddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            "publishedDate": DateInput(attrs={"type:": "date"}),
            "averageRating": TextInput(attrs={"type": "number", "min": "0", "max": "5"})
        }

class ISBNAddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ("isbn",)

class CheckOutForm(forms.Form):
    userId = forms.CharField()
    isbn = forms.CharField()
    class Meta:
        fields = ["userId", "isbn"]