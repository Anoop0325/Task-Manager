from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:id>/assign/', TaskAssignView.as_view(), name='task-assign'),
    path('users/tasks/', UserTasksView.as_view(), name='user-tasks'),
]
