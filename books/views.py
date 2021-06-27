from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Book
from .models import Category

# Create your views here.
def homepage(request):
    #### show the list_books page ~~~
    if request.user.is_authenticated:
        return redirect ("list_books")
    return render(request, "books/homepage.html")


@login_required # this is a decorator or function that will redirect you to login page
def list_books(request):
    books = Book.objects.all()
    ### add category in book lists???
    return render(request, "books/list_books.html",
                  {"books": books})


#### show category

def show_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/show_details.html", {"book": book})


def show_categ(request, slug):
    categ = get_object_or_404(Category, slug=slug)
    #### important!!! 
    books = categ.books.all()

    print(str(books))
    return render(request, "books/show_categ.html", {"categ": categ, "books": books})


### click on favorite ##### 
def favorite_books(request,pk):
    user = request.user
    book = get_object_or_404(Book, pk=pk)
    ####???
    if user.books.filter(id=book.id).exists():
        book.favorites.remove(user)
    ####???
    else:
        book.favorites.add(user)

    return redirect("show_details", pk=pk)

#### show favos  
# class BookDetailView():
#     model = Book
#     template_name = 'show_details.html'

#     def get_context_data(self, *args, **kwargs):
#         stuff= get_object_or_404(Book, id= self.kwargs['pk'])
#         context = super(BookDetailView, self).get_context_data
#         total_favorites = stuff.total_favorites()
#         context['total_favorites'] = total_favorites
#         return context 

