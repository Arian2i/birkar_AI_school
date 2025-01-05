from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=200)  # عنوان ویدئو
    file = models.FileField(upload_to='videos/')  # فایل ویدئو
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)  # کاربری که ویدئو را آپلود کرده

    def __str__(self):
        return self.title  # نمایش عنوان ویدئو