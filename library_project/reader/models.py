from django.db import models


class Reader(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    favorite_books = models.ManyToManyField('book.Book', related_name='readers')

    def __str__(self):
        return self.name
