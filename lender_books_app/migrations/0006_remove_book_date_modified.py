# Generated by Django 2.1.7 on 2019-03-27 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lender_books_app', '0005_book_date_modified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date_modified',
        ),
    ]
