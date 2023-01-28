from django.shortcuts import render

# Create your views here.
def library(request):
    return render(request, "library/library.html")

def new_book(request):
    return render(request, "library/new-book.html")

def check_in(request):
    return render(request, "library/check-in.html")

def check_out(request):
    return render(request, "library/check-out.html")