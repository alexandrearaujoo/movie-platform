from django.db import models

class Review(models.Model):
    start = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomenadation = models.CharField(max_length=50)

    
