from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from session.models import Session

def task_list(request):
    tasks = Task.objects.all() 
    sessions = Session.objects.all()  
    return render(request, 'task/task_list.html', {'tasks': tasks, 'sessions': sessions})

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task/task_detail.html', {'task': task})

def task_create(request, session_id):
    session = get_object_or_404(Session, id=session_id)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.session = session 
            task.save()
            return redirect('session_detail', session_id=session.id)  # بازگشت به جزئیات سشن
    else:
        form = TaskForm()

    return render(request, 'task/task_form.html', {'form': form, 'session_id': session_id})

def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # دریافت تسک بر اساس ID
    session = task.session  # دسترسی به سشن مربوط به تسک

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # ایجاد فرم با داده‌های POST
        if form.is_valid():
            form.save()  # ذخیره تغییرات
            return redirect('session_detail', session_id=session.id)  # بازگشت به جزئیات سشن
    else:
        form = TaskForm(instance=task)  # پر کردن فرم با داده‌های تسک موجود

    return render(request, 'task/task_form.html', {'form': form, 'session_id': session.id})

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # دریافت تسک بر اساس ID
    if request.method == 'POST':
        task.delete()  # حذف تسک
        return redirect('task_list')  # بازگشت به لیست تسک‌ها
    return render(request, 'task/task_confirm_delete.html', {'task': task})
