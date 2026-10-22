# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def book_list(request):
    return render(request, 'crudapp/book_list.html', {'books': Book.objects.all()})

def add_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            price=request.POST['price'],
        )
        return redirect('book_list')
    return render(request, 'crudapp/book_form.html')

def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.price = request.POST['price']
        book.save()
        return redirect('book_list')
    return render(request, 'crudapp/book_form.html', {'book': book})

def delete_book(request, id):
    if request.method == 'POST':
        get_object_or_404(Book, id=id).delete()
    return redirect('book_list')