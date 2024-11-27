from django.db import models

# Create your models here.
class MyProject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/images/')
    date=models.DateField()
    url = models.URLField(blank=True)