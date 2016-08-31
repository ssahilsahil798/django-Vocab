from django.db import models
from django.contrib.auth.models import User
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

class LearntWords(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='learnt')
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='learnt')

    class Meta:
        unique_together = ('user', 'word')

    def __str__(self):
        return self.word.word
