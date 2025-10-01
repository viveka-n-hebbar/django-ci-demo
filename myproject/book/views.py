# books/views.py
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Book

#unittesting view
def hello_book(request):
    return HttpResponse("Hello, Book!")




#example of integration testing viwes


def list_books(request):
    books = Book.objects.all().values("title", "author", "pages")
    return JsonResponse(list(books), safe=False)

def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        pages = int(request.POST.get("pages"))
        Book.objects.create(title=title, author=author, pages=pages)
        return JsonResponse({"message": "Book created"}, status=201)
    return JsonResponse({"error": "Invalid request"}, status=400)

def big_books(request):
    books = Book.objects.filter(pages__gt=300).values("title", "author", "pages")
    return JsonResponse(list(books), safe=False)
