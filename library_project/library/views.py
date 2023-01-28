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
            return redirect("library", )
    else:
        bookForm = ISBNAddBookForm()
    return render(request, "library/new-book-isbn.html", {"bookForm": bookForm})

def check_in(request):
    return render(request, "library/check-in.html")

def check_out(request):
    return render(request, "library/check-out.html")