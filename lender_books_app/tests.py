from django.test import TestCase, RequestFactory
from .models import Book


# Create your tests here.
class TestBookModel(TestCase):

# Is 'setUp' a special django function? It would not pass as 'set_up' or 'setup'.
    def setUp(self):
        Book.objects.create(title='Book Title 1', author='Author', year='1990')
        Book.objects.create(title='Book Title 2', author='Author 2', year='2000')

    def test_book_titles(self):
        book_one = Book.objects.get(title='Book Title 1')
        book_two = Book.objects.get(title='Book Title 2')
        self.assertEqual(book_one.title, 'Book Title 1')
        self.assertEqual(book_two.title, 'Book Title 2')

    def test_book_author(self):
        book_one = Book.objects.get(title='Book Title 1')
        book_two = Book.objects.get(title='Book Title 2')
        self.assertEqual(book_one.author, 'Author')
        self.assertEqual(book_two.author, 'Author 2')

    def test_book_year(self):
        book_one = Book.objects.get(title='Book Title 1')
        book_two = Book.objects.get(title='Book Title 2')
        self.assertEqual(book_one.year, 1990)
        self.assertEqual(book_two.year, 2000)

class TestBookViews(TestCase):
    def setUp(self):
        self.request = RequestFactory()

        Book.objects.create(title='Book Title 1', author='Author', year='1990')
        Book.objects.create(title='Book Title 2', author='Author 2', year='2000')

    def test_book_detail_view_context(self):
        from .views import book_detail_view
        request = self.request.get('')
        response = book_detail_view(request, f'{ Book.objects.get(title="Book Title 1").id }')
        self.assertIn(b'Author', response.content)

    def test_book_list_view_context(self):
        from .views import book_list_view
        request = self.request.get('')
        response = book_list_view(request)
        self.assertIn(b'Book Title 2', response.content)