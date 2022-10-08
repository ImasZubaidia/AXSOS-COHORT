from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # index is the name of a method in views.py
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^new$', views.reg),
    url(r'^logout$', views.logout),
    url(r'^books/(?P<book_id>\d+)$', views.one_book),
    url(r'^books/add_book$', views.add_book),
]