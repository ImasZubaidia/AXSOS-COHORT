from django.shortcuts import render, HttpResponse, redirect
from .models import *
# Create your views here.

def index(request):
    context = {
        "books_DB": Book.objects.all()
    }
    return render(request, "index.html", context)

def addbook(request):
    # print(request.POST)
    Book.objects.create(title = request.POST['booktitle'], desc = request.POST['bookdesc'])
    return redirect('/')

def booksadd(request, bookID):
    context = {
        "books_DB": Book.objects.get(id = bookID),
        "authors_DB": Author.objects.all()
    }
    return render(request, "books.html", context)


def authors(request):
    context = {
        "authors_DB": Author.objects.all()
    }
    return render(request, "authors.html", context)

def addauthor(request):
    print(request.POST)
    Author.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], notes = request.POST['note'])
    return redirect('/authors')

def authorsadd(request, authorID):
    context = {
        "authors_DB": Author.objects.get(id = authorID),
        "books_add": Book.objects.all()
    }
    return render(request, "authorsview.html", context)

def bookstoadd(request, authorID):
    print(request.POST)
    this_book = Book.objects.get(id = request.POST['bookinfo'])
    this_author = Author.objects.get(id = authorID)
    print('******************************', this_book, authorID)
    this_book.link.add(authorID)
    return redirect(f'/authors/{authorID}')

def authorstoadd(request, bookID):
    print(request.POST)
    # this_book = Book.objects.get(id = request.POST['authorinfo'])
    this_author = Author.objects.get(id = request.POST['authorinfo'])
    # this_author = Author.objects.get(id = authorID)
    this_book = Book.objects.get(id = bookID)
    print('******************************', this_author, bookID)
    this_author.books.add(bookID)
    return redirect(f'/book/{bookID}')
