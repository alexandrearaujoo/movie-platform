from django.db import models

class CategoryRecomendation(models.TextChoices):
    MUST_WATCH = ('Must Watch',)
    SHOULD_WATCH = ('Should Watch',)
    AVOID_WATCH = ('Avoid Watch',)
    NO_OPINION = ('No Opinion',)

class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomendation = models.CharField(
        max_length=50, 
        choices=CategoryRecomendation.choices, 
        default=CategoryRecomendation.NO_OPINION
    )

    critic = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='critic')
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE, related_name='movie')


    
