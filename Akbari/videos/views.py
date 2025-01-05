from django.shortcuts import render, redirect, get_object_or_404
from .forms import VideoForm
from .models import Video
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def video_list(request):
    videos = Video.objects.all()  # گرفتن همه ویدئوها
    return render(request, 'videos/video_list.html', {'videos': videos})  # نمایش لیست ویدئوها

@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid() and request.user.is_superuser:  # فقط سوپر یوزرها می‌توانند ویدئو آپلود کنند
            video = form.save(commit=False)
            video.uploaded_by = request.user  # ثبت کاربر آپلودکننده
            video.save()
            return redirect('video_list')  # هدایت به لیست ویدئوها
        else:
            return render(request, 'videos/upload_video.html', {'form': form, 'error': 'شما اجازه آپلود ویدئو ندارید.'})
    else:
        form = VideoForm()
    return render(request, 'videos/upload_video.html', {'form': form})  # نمایش فرم آپلود

def download_video(request, video_id):
    if not request.user.is_authenticated:  # اگر کاربر لاگین نکرده باشد
        return redirect('account_login')  # هدایت به صفحه ورود
    video = get_object_or_404(Video, id=video_id)  # گرفتن ویدئو با ID
    response = HttpResponse(video.file, content_type='video/mp4')  # پاسخ برای دانلود ویدئو
    response['Content-Disposition'] = f'attachment; filename="{video.title}.mp4"' 
    return response
