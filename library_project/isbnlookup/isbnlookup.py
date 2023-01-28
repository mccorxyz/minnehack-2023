#!/usr/bin/python3

import urllib.request
import json
import textwrap

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

        lookup_filters = ["title", "subtitle", "authors", "publisher", "maturityRating", ] #TODO finish list

        with urllib.request.urlopen(base_api_link + isbn_num) as f:
            text = f.read()

        decoded_text = text.decode("utf-8")
        # print(decoded_text)
        obj = json.loads(decoded_text) # deserializes decoded_text to a Python object

        if obj["totalItems"] == 0:
            print("No book found for that ISBN!")
            return None
        rbd = obj["items"][0]
        # authors = obj["items"][0]["volumeInfo"]["authors"]

        # displays title, summary, author, domain, page count and language
        # print("\nTitle:", rbd["volumeInfo"]["title"])
        # print("\nSummary:\n")
        # print(textwrap.fill(book_info["searchInfo"]["textSnippet"], width=65))
        # print("\nAuthor(s):", ",".join(authors))

        # print("\n***")
        # return [book_info["volumeInfo"]["title"]] + obj["items"][0]["volumeInfo"]["authors"]

        # filtered_dict = {k: v for k, v in rbd.iteritems() if filter_string in k}


        return rbd["volumeInfo"]

if __name__ == "__main__":
    print(ISBNLookup().lookup(input("enter isbn")))
