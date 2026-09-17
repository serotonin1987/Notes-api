from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return self.name