from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .user_view import *


def main(request):
    return render(request, 'index.html')


# def book(request):
#     return render(request, 'book/book.html')


class BookLV(LoginRequiredMixin, ListView):
    model = Book
    ordering = ['-created']
    template_name = 'book/book.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)


class BookDV(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'


class BookCV(CreateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'book/book_create.html'


class BookUV(UpdateView):
    model = Book
    form_class = BookForm
    # fields = ['title', 'contents', 'purchase_date', 'read_status']
    template_name_suffix = '_update'

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)


class BookXV(DeleteView):
    models = Book
    queryset = Book.objects.all()
    template_name = 'book/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')
