
# Create your models here.
# books/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    pages = models.IntegerField()

    def is_big_book(self):
        return self.pages > 300
