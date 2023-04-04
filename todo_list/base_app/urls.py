from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (CustomLoginView, RegisterPage, TaskCreate, TaskDelete,
                    TaskDetailView, TaskListView, TaskUpdate)

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]
