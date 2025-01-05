from django.contrib import admin
from .models import Session

class SessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'course')
    search_fields = ('name',)

admin.site.register(Session, SessionAdmin)
