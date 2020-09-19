from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class BooksModel(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    createdAt = models.DateField(auto_now_add=True)
    publication_date = models.DateField()

    def __str__(self):
        return f"{self.title} == > {self.author}"


class BookReviews(models.Model):

    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    review = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    ebook = models.ForeignKey(
        BooksModel, on_delete=models.CASCADE, related_name="reviews"
    )

    def __str__(self):
        return f"{self.rating}"
