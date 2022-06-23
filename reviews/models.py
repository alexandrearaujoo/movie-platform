from django.db import models

class CategoryRecomendation(models.TextChoices):
    MUST_WATCH = ('must watch',)
    SHOULD_WATCH = ('should watch',)
    AVOID_WATCH = ('avoid watch',)
    NO_OPINION = ('no opinion',)

class Review(models.Model):
    starts = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomenadation = models.CharField(
        max_length=50, 
        choices=CategoryRecomendation.choices, 
        default=CategoryRecomendation.NO_OPINION
    )

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='users')


    
