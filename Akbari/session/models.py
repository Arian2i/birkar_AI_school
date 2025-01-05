from django.db import models
from course.models import Course

class Session(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name='sessions', on_delete=models.CASCADE)

    def __str__(self):
        return self.name