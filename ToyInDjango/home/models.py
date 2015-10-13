from django.db import models

# Create your models here.

class Sentence(models.Model):
    sentence = models.CharField(max_length=200)

    #To control what will be showed on the screen
    def __str__(self):
        return self.sentence
