from django.db import models

# Create your models here.

class CardCategory(models.Model):

    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Word(models.Model):

    category = models.ForeignKey(CardCategory, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    meaning = models.CharField(max_length=500)

    def __str__(self):
        return self.word


