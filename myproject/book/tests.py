# books/tests.py
from django.test import TestCase
from .models import Book

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



# books/tests.py
from django.test import TestCase
from django.urls import reverse

class BookViewTest(TestCase):

    def test_hello_book_view(self):
        url = reverse('hello_book')         # Get URL for view
        response = self.client.get(url)     # Make GET request
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, Book!")





















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