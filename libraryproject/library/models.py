from django.db import models

class Book (models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=250)
    pages = models.CharField(max_length=500)
    isActive = models.CharField(max_length=50)





