from django.db import models

# Create your models here.
class CurrentResearch(models.Model):
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title