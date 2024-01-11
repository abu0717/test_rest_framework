from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=10)
    email = models.EmailField()
