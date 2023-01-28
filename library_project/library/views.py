from django.shortcuts import render
from isbnlookup.isbnlookup import ISBNLookup
from django.contrib import messages

# Create your views here.
def library(request):
    return render(request, "library/library.html")

def new_book(request):

    if request.method == "POST":
        bookForm = BookForm(request.POST)
        if bookForm.is_valid():
            ISBNLookup().lookup(bookForm.isbn)
            messages.info(request, "Adding book!")
            bookForm.save()
            return redirect("library")
    return render(request, "library/new-book.html")

def check_in(request):
    return render(request, "library/check-in.html")

def check_out(request):
    return render(request, "library/check-out.html")