from django.db import models

class Course(models.Model):
    duration = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher_page = models.CharField(max_length=50)

    def __str__(self):
        return self.name