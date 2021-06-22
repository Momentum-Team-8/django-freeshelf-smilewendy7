from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book (models.Model):
    # artist= models.ManyToManyField(
    #     "Artist",
    #     on_delete=models.CASCADE,
    #     related_name="albums",
    #     #### this step is important!!!! means artist_id can be null.
    #     null=True,
    # )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    created_at =models.DateTimeField(auto_now_add=False)
    book_url =models.CharField(max_length=255)

    def __str__(self):
        ### this change how it looks in shell
        return f"Author Name ={self.author}"

    def __str__(self):
        return self.title

