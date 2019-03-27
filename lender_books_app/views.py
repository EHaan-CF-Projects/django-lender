from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Book

# Create your views here.
def book_list_view(request):
    context = {
        'books' : get_list_or_404(Book),
    }
    return render(request, 'books/book_list.html', context)

def book_detail_view(request, pk=None):
    context = {
        'book' : get_object_or_404(Book, pk=id),
    }
    return render(request, 'books/book_detail.html', context)