from django.shortcuts import render, redirect
from isbnlookup.isbnlookup import ISBNLookup
from django.contrib import messages
from .forms import *

# Create your views here.
def library(request):
    return render(request, "library/library.html")

def new_user(request):
    return render(request, "library/new-user.html")

def new_book(request):
    return render(request, "library/new-book.html", {"ISBNForm": ISBNAddBookForm(), "manualForm": ManualAddBookForm()})


def new_book_manual(request):
    if request.method == "POST":
        bookForm = ManualAddBookForm(request.POST)
        if bookForm.is_valid():
            print(bookForm.cleaned_data["title"])
            existingBookList = Book.objects.filter(title=bookForm.cleaned_data["title"])
            if len(existingBookList) > 0:
                mBook = existingBookList[0]
                mBook.quantity += 1
                messages.info(request, "You now have {} copies of {}".format(mBook.quantity, mBook.title))
                mBook.save()
            else:
                bookForm.save()
                messages.info(request, "Added {} to your library".format(bookForm.cleaned_data["title"]))

    return redirect("newBook",)

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
                existingBookList = Book.objects.filter(isbn=bookForm.cleaned_data["isbn"])
                if len(existingBookList) > 0:
                    mBook = existingBookList[0]
                    mBook.quantity += 1
                    messages.info(request, "You now have {} copies of {}".format(mBook.quantity, mBook.title))
                    mBook.save()
                else:
                    Book(**bookDict).save()
                    messages.info(request, "Added {} to your library".format(bookDict["title"]))

    return redirect("newBook", )

def check_in(request):
    if request.method == "POST":
        checkInForm = CheckInForm(request.POST)
        if checkInForm.is_valid():
            print('hello')
    else:
        checkInForm = CheckInForm()
    return render(request, "library/check-in.html", { "form": checkInForm })

def check_out(request):
    if request.method == "POST":
        checkOutForm = CheckOutForm(request.POST)
        if checkOutForm.is_valid():
            print(checkOutForm.cleaned_data["card_id"])
            print(checkOutForm.cleaned_data["isbns"][0])
            desiredBookList = Book.objects.filter(isbn=checkOutForm.cleaned_data["isbns"][0])
            if len(desiredBookList) > 0:
                userList = User.objects.filter(card_id=checkOutForm.cleaned_data["card_id"])
                if len(userList) > 0:
                    userList.isbns += checkOutForm.cleaned_data["isbns"]
                    userList.save()
                    messages.info(request, "Checkout out {} to {}".format(desiredBookList[0]["title"], userList[0]["name"]))
                else:
                    messages.info(request, "Invalid card id")

            else:
                messages.info(request, "Book with entered ISBN is not in your library")
        return redirect("checkOut")
    else:
        checkOutForm = CheckOutForm()
    return render(request, "library/check-out.html", {"form": checkOutForm})