from django.urls import path
from .views import session_list, session_detail, session_create, session_update, session_delete

urlpatterns = [
    path('', session_list, name='session_list'),
    path('new/', session_create, name='session_create'),
    path('<int:session_id>/', session_detail, name='session_detail'),
    path('<int:session_id>/edit/', session_update, name='session_update'),
    path('<int:session_id>/delete/', session_delete, name='session_delete'),
]