from django.db import models


# Create your models here.
class Book(models.Model):
    """
    """
    title = models.CharField(max_length=48)
    author = models.CharField(max_length=48)
    year = models.IntegerField(max_length=4)

    STATES = [
        ('available', 'Available'),
        ('checked out', 'Checked Out'),
    ]

    status = models.CharField(choices=STATES, default='available', max_length=48)

    def __repr__(self):
        return f'<Book: {self.title} | Status: {self.status}>'

    def __str__(self):
        return f'Book: {self.title} | Status: {self.status}'