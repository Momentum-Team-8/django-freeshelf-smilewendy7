from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book (models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    created_at =models.DateTimeField(auto_now_add=False)
    book_url =models.CharField(max_length=255)

    def __str__(self):
        return self.title

