from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    """
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=48)
    author = models.CharField(max_length=48)
    year = models.IntegerField(default=0000)

    STATES = [
        ('available', 'Available'),
        ('checked out', 'Checked Out'),
    ]

    status = models.CharField(choices=STATES, default='available', max_length=48)

    date_added = models.DateTimeField(default=now)
    last_borrowed = models.DateTimeField(auto_now=True)


    def __repr__(self):
        return f'<Book: {self.title} | Status: {self.status}>'

    def __str__(self):
        return f'Book: {self.title} | Status: {self.status}'

