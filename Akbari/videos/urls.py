from django.urls import path
from .views import upload_video, video_list, download_video

urlpatterns = [
    path('', video_list, name='video_list'),  # صفحه اصلی: لیست ویدئوها
    path('upload/', upload_video, name='upload_video'),  # صفحه آپلود ویدئو
    path('download/<int:video_id>/', download_video, name='download_video'),  # دانلود ویدئو
]