from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book (models.Model):
    category = models.ManyToManyField(
        "Category",
        # on_delete=models.CASCADE,
        related_name="books",
        #### this step is important!!!! means category_id can be null.
        # null=True,
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    created_at =models.DateTimeField(auto_now_add=False)
    book_url =models.CharField(max_length=255)

    def __str__(self):
        ### this change how it looks in shell
        return f"Author Name ={self.title}"

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Category (models.Model):
    category_name = models.CharField(max_length=255)
    ### add slug
    slug = models.SlugField(max_length=75,null=True)

    def __str__(self):
        return f"<Category name = {self.category_name}>"

    def __str__(self):
        return self.category_name

