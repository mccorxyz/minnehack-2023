from library.models import Book
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from isbnlookup.isbnlookup import *


# Create your views here.
@api_view(['POST'])
def post_new_book(request, isbn):
    if request.method == "POST":
        bookDict = ISBNLookup().lookup(isbn)
        if bookDict is None:
            return JsonResponse({"success": "false"})
        else:
            book = Book.objects.filter(isbn=isbn)
            if len(book) == 0:
                Book(**bookDict).save()
            else:
                book[0].quantity += 1
                book[0].save()
            return JsonResponse({"success": "true"})
