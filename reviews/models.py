from django.db import models

class Review(models.Model):
    starts = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomenadation = models.CharField(max_length=50)

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='users')


    
