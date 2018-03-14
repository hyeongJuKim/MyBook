from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .user_view import UserCV, UserDV


def main(request):
    return render(request, 'index.html')


# def book(request):
#     return render(request, 'book/book.html')


class BookLV(ListView):
    model = Book
    template_name = 'book/book.html'
    context_object_name = 'books'
    # paginate_by = 10  # 페이징


class BookDV(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'


class BookCV(CreateView):
    model = Book
    fields = ['title', 'contents', 'user']
    template_name = 'book/book_create.html'


class BookUV(UpdateView):
    model = Book
    fields = ['title', 'contents']
    template_name_suffix = '_update'


class BookXV(DeleteView):
    models = Book
    queryset = Book.objects.all()
    template_name = 'book/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')
