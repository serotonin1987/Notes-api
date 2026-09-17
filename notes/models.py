from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    description = models.CharField(
        max_length=200,
        blank=True,
        null=True
        )
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    description = models.CharField(
        max_length=200,
        blank=True,
        null=True
        )
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title