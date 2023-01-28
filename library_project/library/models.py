from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField

from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField
from django.core.exceptions import ValidationError

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    #author = models.ForeignKey()
    publisher = models.CharField(max_length=100)
    publishedDate = ArrayField(models.DateField())
    description = models.CharField(max_length=500)
    isbn = models.CharField(max_length=13)
    pageCount = models.IntegerField(default=0,
                                    validators=[
                                        MinValueValidator(0)
                                    ])
    categories = ArrayField(models.CharField(max_length=20))
    # averageRating = models.DecimalField(default=0,
    #                                     validators=[
    #                                         MinValueValidator(0),
    #                                         MaxValueValidator(5)
    #                                     ])
    maturity = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=200)
    publicDomain = models.BooleanField()

class Author(models.Model):
    name = models.CharField(max_length=100)



