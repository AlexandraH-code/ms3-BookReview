from django.shortcuts import render, get_object_or_404
from .models import Book, Review  # Import the models
from django.http import HttpResponse


# Create your views here.
def my_books(request):
    return HttpResponse("Hello, Books!")


def books_list(request):
    books = Book.objects.filter(is_draft=False)  # Fetch only published books
    return render(request, 'books.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.reviews.filter(approved=True)  # Show only approved reviews
    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews})
