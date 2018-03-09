from django.shortcuts import render


def main(request):
    return render(request, 'index.html')


def book(request):
    return render(request, 'book.html')
