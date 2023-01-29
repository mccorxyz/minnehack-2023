from django.shortcuts import render, redirect
from isbnlookup.isbnlookup import ISBNLookup
from django.contrib import messages
from .forms import *

# Create your views here.
def library(request):
    return render(request, "library/library.html")

def new_user(request):
    return render(request, "library/new-user.html")

def new_book_manual(request):
    return render(request, "library/new-book-manual.html")

def new_book_isbn(request):
    if request.method == "POST":
        bookForm = ISBNAddBookForm(request.POST)
        if bookForm.is_valid():
            print(bookForm.cleaned_data["isbn"])
            bookDict = ISBNLookup().lookup(bookForm.cleaned_data["isbn"])

            if bookDict is None:
                # Do error
                messages.info(request, "Error, could not add book")
            else:
                # print(str(bookDict))
                existingBookList = Book.objects.filter(isbn=bookForm.cleaned_data["isbn"])
                if len(existingBookList) > 0:
                    mBook = existingBookList[0]
                    mBook.quantity += 1
                    messages.info(request, "You now have {} copies of {}".format(mBook.quantity, mBook.title))
                    mBook.save()
                else:
                    Book(**bookDict).save()
                    messages.info(request, "Added {} to your library".format(bookDict["title"]))

            return redirect("newBookISBN", )
    else:
        bookForm = ISBNAddBookForm()
    return render(request, "library/new-book-isbn.html", {"bookForm": bookForm})

def check_in(request):
    return render(request, "library/check-in.html")

def check_out(request):
    return render(request, "library/check-out.html")