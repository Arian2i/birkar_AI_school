from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'session')
    search_fields = ('name',)

admin.site.register(Task, TaskAdmin)