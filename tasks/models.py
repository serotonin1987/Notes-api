from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title