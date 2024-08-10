from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField(validators=[MinValueValidator(0)])
    is_bestselling = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.author} {self.year}"

    class Meta:
        db_table = 'book'
