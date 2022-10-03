
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"<Author object: {self.first_name} {self.last_name}({self.id})>"


class Book(models.Model):
    title = models.CharField(max_length=255, blank=True)
    desc = models.TextField(blank=True)
    link = models.ManyToManyField(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"<Book object: {self.title} {self.desc}({self.id})>"
