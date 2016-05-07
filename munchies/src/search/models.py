from django.db import models

class Product (models.Model):
    asin = models.CharField(max_length=10)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=5000)
    url = models.URLField()

    def __str__(self):
        return self.title