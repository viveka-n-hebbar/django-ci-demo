# books/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_book, name='hello_book'),
]
