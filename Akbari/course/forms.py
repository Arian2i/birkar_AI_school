from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['duration', 'level', 'name', 'description', 'teacher_page']