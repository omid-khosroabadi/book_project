from django.db import models
from django.urls import reverse


class Books(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='book_image/', blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])


class Comment(models.Model):
    STAR = (
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'normal'),
        ('4', 'good'),
        ('5', 'perfect'),
    )
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='comments')
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    star = models.CharField(max_length=10, choices=STAR)
    recommend = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.book.id])

