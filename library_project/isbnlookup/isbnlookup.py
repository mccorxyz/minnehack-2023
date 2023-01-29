#!/usr/bin/python3

import urllib.request
# import requests
import json
import textwrap

# from http import cookiejar  # Python 2: import cookielib as cookiejar
#
# class BlockAll(cookiejar.CookiePolicy):
#     return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
#     netscape = True
#     rfc2965 = hide_cookie2 = False

class ISBNLookup:

    def __init__(self):
        pass

    def lookup(self, isbn_num:str):
        """
        Given an ISBN number (ISBN 10 or 13), return a dictionary object:
        TODO figure out dict structure
        :param isbn_num:
        :return:
        """

        base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

        print(base_api_link + isbn_num)

        with urllib.request.urlopen(base_api_link + isbn_num) as f:
            text = f.read()


        decoded_text = text.decode("utf-8")
        obj = json.loads(decoded_text) # deserializes decoded_text to a Python object

        if obj["totalItems"] == 0:
            print("No book found for that ISBN!")
            return None

        b_obj = obj["items"][0]

        # print("b_obj: {}".format(b_obj))

        b_dict = {
            "title": b_obj["volumeInfo"]["title"],
            "author": b_obj["volumeInfo"]["author"],
            "subtitle": b_obj["volumeInfo"]["title"],
            "publisher": b_obj["volumeInfo"]["publisher"],
            "publishedDate": b_obj["volumeInfo"]["publishedDate"],
            "description": b_obj["volumeInfo"]["description"],
            "isbn": isbn_num,
            "pageCount": b_obj["volumeInfo"]["pageCount"],
            "categories": b_obj["volumeInfo"]["categories"],
            "maturityRating": b_obj["volumeInfo"]["maturityRating"],
            "averageRating": b_obj["volumeInfo"]["averageRating"],
            "thumbnail": b_obj["volumeInfo"]["imageLinks"]["thumbnail"],
            "publicDomain": b_obj["accessInfo"]["publicDomain"],
        }
        # rbd = obj["items"][0]
        # authors = obj["items"][0]["volumeInfo"]["authors"]

        # displays title, summary, author, domain, page count and language
        # print("\nTitle:", rbd["volumeInfo"]["title"])
        # print("\nSummary:\n")
        # print(textwrap.fill(book_info["searchInfo"]["textSnippet"], width=65))
        # print("\nAuthor(s):", ",".join(authors))

        # print("\n***")
        # return [book_info["volumeInfo"]["title"]] + obj["items"][0]["volumeInfo"]["authors"]

        # filtered_dict = {k: v for k, v in rbd.iteritems() if filter_string in k}

        # print("about to return")
        return b_dict

if __name__ == "__main__":
    print(ISBNLookup().lookup(input("enter isbn")))
