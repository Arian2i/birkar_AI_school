from django.shortcuts import render, get_object_or_404, redirect
from .models import Session
from .forms import SessionForm

def session_list(request):
    sessions = Session.objects.all()
    sessions=[]
    return render(request, 'session/session_list.html', {'sessions': sessions})

def session_detail(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    return render(request, 'session/session_detail.html', {'session': session})

def session_create(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('session_list')
    else:
        form = SessionForm()
    return render(request, 'session/session_form.html', {'form': form})

def session_update(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    if request.method == 'POST':
        form = SessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('session_detail', session_id=session.id)
    else:
        form = SessionForm(instance=session)
    return render(request, 'session/session_form.html', {'form': form})

def session_delete(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    if request.method == 'POST':
        session.delete()
        return redirect('session_list')
    return render(request, 'session/session_confirm_delete.html', {'session': session})
