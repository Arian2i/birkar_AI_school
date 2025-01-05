from django.db import models
from session.models import Session

class Task(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    content = models.TextField()
    session = models.ForeignKey(Session, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
