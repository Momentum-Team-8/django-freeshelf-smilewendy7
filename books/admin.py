from books.models import User
from django.contrib import admin
from .models import User
from .models import Book
from .models import Category


# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Category)

