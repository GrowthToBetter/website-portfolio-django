from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class MyProject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')
    date=models.DateField()
    url = models.URLField(blank=True)