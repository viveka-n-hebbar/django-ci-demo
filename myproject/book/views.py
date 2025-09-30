# books/views.py
from django.http import HttpResponse

def hello_book(request):
    return HttpResponse("Hello, Book!")
