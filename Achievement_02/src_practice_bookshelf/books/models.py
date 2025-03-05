from django.db import models
from django.shortcuts import reverse


class Book(models.Model):
    GENRE_CHOICES = [
        ('classic', 'Classic'),
        ('romantic', 'Romantic'),
        ('comic', 'Comic'),
        ('fantasy', 'Fantasy'),
        ('horror', 'Horror'),
        ('educational', 'Educational'),
    ]

    BOOK_TYPE_CHOICES = [
        ('hardcover', 'Hardcover'),
        ('ebook', 'E-Book'),
        ('audiobook', 'Audiobook'),
    ]

    name = models.CharField(max_length=120)
    genre = models.CharField(
        max_length=12, choices=GENRE_CHOICES, default='classic')
    book_type = models.CharField(
        max_length=12, choices=BOOK_TYPE_CHOICES, default='hardcover')
    price = models.FloatField(help_text="in US dollars $")
    author_name = models.CharField(max_length=120)
    pic = models.ImageField(upload_to='books', default='no_picture.jpg')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'pk': self.pk})
