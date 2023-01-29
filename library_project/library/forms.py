from django.forms import ModelForm, DateInput, TextInput
from django import forms
from .models import Book, User


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

class CheckInForm(forms.Form):
    card_id = forms.CharField()
    isbn = forms.CharField()
    class Meta:
        fields = ["card_id", "isbn",]

class CheckOutForm(forms.Form):
    card_id = forms.CharField()
    isbn = forms.CharField()
    class Meta:
        fields = ["card_id", "isbn",]

class NewUserForm(ModelForm):
    class Meta:
        model = User
        fields = ("name", "card_id")

class ViewUserBooksForm(ModelForm):
    class Meta:
        model = User
        fields = ("card_id",)

# class CheckoutBookForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ("isbns", "card_id",)