from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('book/add', views.addbook),
    path('book/<int:bookID>', views.booksadd),
    path('authors', views.authors),
    path('authors/add', views.addauthor),
    path('authors/<int:authorID>', views.authorsadd),
    path('bookstoadd/<int:authorID>', views.bookstoadd),
    path('authorstoadd/<int:bookID>', views.authorstoadd)
]