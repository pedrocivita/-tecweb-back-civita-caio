from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    fav = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + " - " + self.title