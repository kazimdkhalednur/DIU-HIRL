from django.db import models

# Create your models here.
class CurrentResearch(models.Model):
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=1000)
    caption = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to="img/%y",null=True)

    def __str__(self):
        return self.title