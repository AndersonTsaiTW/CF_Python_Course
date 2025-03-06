from django.shortcuts import render  # imported by default
# to display lists and details  # to display lists
from django.views.generic import ListView, DetailView
from .models import Book  # to access Book model

# to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class BookListView(LoginRequiredMixin, ListView):   # class-based view
    model = Book  # specify model
    template_name = 'books/main.html'  # specify template


class BookDetailView(LoginRequiredMixin, DetailView):  # class-based “protected” view
    model = Book  # specify model
    template_name = 'books/detail.html'  # specify template
