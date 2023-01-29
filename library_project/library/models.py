from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField

from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField
from django.core.exceptions import ValidationError

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    author = models.ManyToManyField(Author)
    publisher = models.CharField(max_length=100)
    publishedDate = models.DateField
    description = models.CharField(max_length=500)
    isbn = models.CharField(max_length=13)
    pageCount = models.IntegerField(default=0,
                                    validators=[
                                        MinValueValidator(0)
                                    ])
    categories = models.JSONField()
    averageRating = models.DecimalField(default=0,
                                        decimal_places=1,
                                        max_digits=2,
                                        validators=[
                                            MinValueValidator(0),
                                            MaxValueValidator(5)
                                        ])
    maturity = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=200)
    publicDomain = models.BooleanField()
    quantity = models.IntegerField(default=0,
                                   validators=[
                                       MinValueValidator(0)
                                   ])

class Student(models.Model):
    name = models.CharField(max_length=100)
    isbns = models.JSONField()


