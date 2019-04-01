from django.test import TestCase, RequestFactory
from .models import Book
from django.contrib.auth.models import User
from .views import book_detail_view, book_list_view
from django.http import Http404


# Create your tests here.
class TestBookModel(TestCase):
    def setUp(self):
        user = User.objects.create_user('Kaja', 'Schwartzekatze')
        Book.objects.create(title='Book Title 1', author='Author', year='1990', user=user)
        Book.objects.create(title='Book Title 2', author='Author 2', year='2000', user=user)

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

    def test_book_user(self):
        book_one = Book.objects.get(title='Book Title 1')
        book_two = Book.objects.get(title='Book Title 2')
        self.assertEqual(book_one.user.username, 'Kaja')
        self.assertEqual(book_two.user.username, 'Kaja')


class TestBookViews(TestCase):
    def setUp(self):
        self.request = RequestFactory()
        self.user = User.objects.create_user('Kaja', 'Schwartzekatze')
        Book.objects.create(title='Book Title 1', author='Author', year='1990', user=self.user)
        Book.objects.create(title='Book Title 2', author='Author 2', year='2000', user=self.user)

    # Book Detail View Tests
    def test_book_detail_view_context(self):
        request = self.request.get('')
        request.user = self.user
        response = book_detail_view(request, f'{ Book.objects.get(title="Book Title 1").id }')
        self.assertIn(b'Author', response.content)

    def test_book_detail_view_status_code(self):
        request = self.request.get('')
        request.user = self.user
        response = book_detail_view(request, f'{Book.objects.get(title="Book Title 1").id }')
        self.assertEqual(response.status_code, 200)

    # -------------------------->>> pls explain this test? (and see below)
    def test_book_detail_view_failure(self):
        request = self.request.get('')
        request.user = self.user
        with self.assertRaises(Http404):
            book_detail_view(request, '0')

    # Book List View Tests
    def test_book_list_view_context(self):
        request = self.request.get('')
        request.user = self.user
        response = book_list_view(request)
        self.assertIn(b'Book Title 2', response.content)

    def test_book_list_view_status_code(self):
        request = self.request.get('')
        request.user = self.user
        response = book_list_view(request)
        self.assertEqual(response.status_code, 200)
        
    # ----------------------------->>> and why it does not work the same here -- and why does the error show up for a different test?
    # def test_book_list_view_failure(self):
    #     request = self.request.get('')
    #     request.user = self.user
    #     with self.assertRaises(Http404):
    #         book_list_view(request)
        
