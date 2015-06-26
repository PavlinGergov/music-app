from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length = 64, null=True)
    image = models.ImageField()
    created = models.DateField()
    location = models.CharField(max_length = 32,null=True)
    albums = models.SmallIntegerField(default=0)
    singles = models.SmallIntegerField(default=0)
