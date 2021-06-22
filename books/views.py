from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Book

# Create your views here.
def homepage(request):
    #### show the list_books page ~~~
    if request.user.is_authenticated:
        return redirect ("list_books")
    return render(request, "books/homepage.html")


@login_required # this is a decorator or function that will redirect you to login page
def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html",
                  {"books": books})
