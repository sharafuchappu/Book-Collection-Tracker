from django.shortcuts import render, redirect
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        genre = request.POST['genre']
        publication_year = request.POST['publication_year']
        Book.objects.create(title=title, author=author, genre=genre, publication_year=publication_year)
        return redirect('home')
    return render(request, 'books/add_book.html')

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('home')
