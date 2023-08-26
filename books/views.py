from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from . import models


class BookList(ListView):
    model = models.Book
    template_name = "books/book_list.html"
    context_object_name = "books"
