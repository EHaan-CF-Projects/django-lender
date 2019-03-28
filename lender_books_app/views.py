from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book

# Create your views here.
@login_required
def book_list_view(request):
    context = {
        'books': get_list_or_404(Book, user=request.user.id),
    }
    return render(request, 'books/book_list.html', context)


@login_required
def book_detail_view(request, pk=None):
    context = {
        'book': get_object_or_404(Book, id=pk, user=request.user.id),
    }
    return render(request, 'books/book_detail.html', context)
