from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=12)

    def __str__(self):
        return self.name