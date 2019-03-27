from django.test import TestCase
from .models import Book


# Create your tests here.
class TestBookModel(TestCase):

    def test_book_titles(self):
        Book.objects.create(title='Book Title 1', author='Author', year='1990')
        Book.objects.create(title='Book Title 2', author='Author 2', year='2000')
        book1 = Book.objects.get(title='Book Title 1')
        book2 = Book.objects.get(title='Book Title 2')
        self.assertEqual(book1.title, 'Book Title 1')
        self.assertEqual(book2.title, 'Book Title 2')

