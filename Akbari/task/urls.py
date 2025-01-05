from django.urls import path
from .views import task_list, task_detail, task_create, task_update, task_delete

urlpatterns = [
    path('', task_list, name='task_list'),  # لیست تسک‌ها
    path('new/<int:session_id>/', task_create, name='task_create'),  # ایجاد تسک جدید
    path('<int:task_id>/', task_detail, name='task_detail'),  # جزئیات تسک
    path('<int:task_id>/update/', task_update, name='task_update'),  # ویرایش تسک
    path('<int:task_id>/delete/', task_delete, name='task_delete'),  # حذف تسک
]