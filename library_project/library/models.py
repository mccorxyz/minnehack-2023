from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField

from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField
from django.core.exceptions import ValidationError

# Create your models here.
# class Author(models.Model):
#     name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    # authors = models.ManyToManyField(Author)
    authors = models.JSONField()
    publisher = models.CharField(max_length=100)
    # publishedDate = models.DateField
    publishedDate = models.CharField(max_length=20)
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
    maturityRating = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=200)
    publicDomain = models.BooleanField()
    quantity = models.IntegerField(default=0,
                                   verbose_name="Copies",
                                   validators=[
                                       MinValueValidator(0)
                                   ])

class User(models.Model):
    name = models.CharField(max_length=100)
    isbns = models.JSONField(default=list)
    card_id = models.CharField(max_length=50)


