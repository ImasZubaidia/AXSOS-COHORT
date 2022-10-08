
from __future__ import unicode_literals
from django.db import models
import re

class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['book_title']) < 1:
            errors["title"] = "title should exist"
        if len(postData['book_description']) < 5:
            errors["description"] = "description should be at least 5 characters"
        return errors


class Book(models.Model):
    objects = BookManager()
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __repr__(self):
        return f"<Book object: {self.title}, description: {self.description}>"
        

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        for existing_user in User.objects.all():
            if existing_user.email == postData['email']:
                errors["email_exists"] = "We already have a user with this email"
        if len(postData['first_name']) < 2:
            errors["first_name"] = "first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "last name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Invalid email address!")
        return errors


class User(models.Model):
    objects = UserManager()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    fav_books = models.ManyToManyField(Book, related_name="fans")
    # email = models.EmailField(max_length=255) TODO: read up on this
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __repr__(self):
        return f"<User Object: {self.first_name} {self.last_name}, email: {self.email} password: {self.password}>"