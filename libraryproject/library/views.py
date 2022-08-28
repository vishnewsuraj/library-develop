from urllib import request
from django.shortcuts import render
from .models import *



def index(request):
    return render(request, 'index.html')



def addBook (request):
    if request.method == "POST":
        name = request.POST['name']
        author = request.POST['author']
        pages = request.POST['pages']
        isActive = request.POST['isActive']
 
        books = Book.objects.create(name=name, author=author, pages=pages, isActive=isActive)
        books.save()
        alert = True
        return render(request, "addBook.html", {'alert':alert})
    return render(request, "addBook.html")



def viewBooks(request):
    books = Book.objects.all()
    return render(request, "viewBook.html", {'books':books})