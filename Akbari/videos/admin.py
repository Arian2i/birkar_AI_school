from django.contrib import admin
from .models import Video  # وارد کردن مدل ویدئو

# ثبت مدل ویدئو در پنل مدیریت
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'id')  # نمایش فیلدهای عنوان، کاربر آپلودکننده و ID
    search_fields = ('title',)  # قابلیت جستجو بر اساس عنوان
