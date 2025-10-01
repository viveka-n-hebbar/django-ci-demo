# books/tests.py
from django.test import TestCase
from .models import Book
from django.test import TestCase
from django.urls import reverse
import json

#unit testing example1 for model
class BookModelTest(TestCase):
    def test_is_big_book(self):
        # Arrange → create a Book object
        book = Book.objects.create(title="Small Book", author="John", pages=150)

        # Act → call the method
        result = book.is_big_book()

        # Assert → check the result
        self.assertFalse(result)   # book with 150 pages is NOT big

    def test_is_big_book_true(self):
        book = Book.objects.create(title="Big Book", author="Alice", pages=500)
        result = book.is_big_book()
        self.assertTrue(result)    # 500 pages IS a big book
'''    def test_is_big_book_fail(self):
        book = Book.objects.create(title="Tiny Book", author="Mark", pages=100)
        result = book.is_big_book()
        self.assertTrue(result)   #''' 


#unit testing example2 for views
class BookViewTest(TestCase):

    def test_hello_book_view(self):
        url = reverse('hello_book')         # Get URL for view
        response = self.client.get(url)     # Make GET request
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, Book!")




#integration testing complete


class BookIntegrationTest(TestCase):
    def setUp(self):
        # Preload some books into the DB
        Book.objects.create(title="Small Book", author="Alice", pages=150)
        Book.objects.create(title="Big Book", author="Bob", pages=500)

    def test_model_method_integration(self):
        """Check model method works after saving to DB"""
        book = Book.objects.get(title="Big Book")
        self.assertTrue(book.is_big_book())   # >300 pages
        book2 = Book.objects.get(title="Small Book")
        self.assertFalse(book2.is_big_book()) # <=300 pages

    def test_list_books_view(self):
        """Check if list_books view returns all books"""
        url = reverse("books_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["author"], "Alice")

    def test_add_book_view(self):
        """Check if POST creates a new book"""
        url = reverse("add_book")
        response = self.client.post(url, {
            "title": "Django Mastery",
            "author": "Charlie",
            "pages": 350
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 3)  # now 3 books

    def test_big_books_view(self):
        """Check if big_books view returns only >300 page books"""
        url = reverse("big_books")
        response = self.client.get(url)
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], "Big Book")


















#if you want less code use this setup function 
'''from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):

    def setUp(self):
        # This runs before every test
        self.small_book = Book.objects.create(title="Small Book", author="John", pages=150)
        self.big_book = Book.objects.create(title="Big Book", author="Alice", pages=500)

    def test_small_book_is_not_big(self):
        result = self.small_book.is_big_book()
        self.assertFalse(result)

    def test_big_book_is_big(self):
        result = self.big_book.is_big_book()
        self.assertTrue(result)
'''