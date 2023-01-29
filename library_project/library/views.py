from django.shortcuts import render, redirect
from isbnlookup.isbnlookup import ISBNLookup
from django.contrib import messages
from .forms import *

# Create your views here.
def library(request):
    return render(request, "library/library.html")

def new_book_manual(request):
    return render(request, "library/new-book-manual.html")

def new_book_isbn(request):
    if request.method == "POST":
        bookForm = ISBNAddBookForm(request.POST)
        if bookForm.is_valid():
            print(bookForm.cleaned_data["isbn"])
            # ISBNLookup().lookup(bookForm.cleaned_data["isbn"])
            messages.info(request, "Adding book!")
            # bookForm.save()
            return redirect("newBookISBN", )
    else:
        bookForm = ISBNAddBookForm()
    return render(request, "library/new-book-isbn.html", {"form": bookForm})

def check_in(request):
    return render(request, "library/check-in.html")

def check_out(request):
    if request.method == "POST":
        checkOutForm = CheckOutForm(request.POST)
        if checkOutForm.is_valid():
            print('hello')
    else:
        checkOutForm = CheckOutForm()
    return render(request, "library/check-out.html", {"form": checkOutForm})