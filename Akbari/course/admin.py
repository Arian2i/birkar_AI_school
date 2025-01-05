from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'level')
    search_fields = ('name',)

admin.site.register(Course, CourseAdmin)