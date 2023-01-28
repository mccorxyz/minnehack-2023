from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    # authors
    publisher = models.CharField(max_length=100)
    publishedDate = models.DateField
    description = models.CharField(max_length=500)
    isbn = models.CharField(max_length=13)
    pageCount = models.IntegerField(default=0,
                                    validators=[
                                        MinValueValidator(0)
                                    ])
    # categories
    averageRating = models.DecimalField(default=0,
                                        validators=[
                                            MinValueValidator(0),
                                            MaxValueValidator(5)
                                        ])
    # maturity



class BookForm(models.Model):
    isbn = models.CharField(max_length=13)