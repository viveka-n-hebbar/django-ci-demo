# books/urls.py
from django.urls import path
from . import views
from django.urls import path
from .views import list_books, add_book, big_books

urlpatterns = [
    path('hello/', views.hello_book, name='hello_book'),

    
    path("books/", list_books, name="books_list"),
    path("books/add/", add_book, name="add_book"),
    path("books/big/", big_books, name="big_books"),
]
