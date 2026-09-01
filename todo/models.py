from django.db import models
from django.utils import timezone

# creating a todo model


class Todos(models.Model):

    todo = models.CharField(max_length=255)
    detail = models.TextField(blank=True, default='')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.todo
