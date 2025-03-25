from django.db import models
from django.contrib.auth.models import AbstractUser


TASK_TYPES = (
        ('P', 'Personal'),
        ('W', 'Work'),
        ('S', 'Shopping'),
        ('O', 'Other'),
    )
    
STATUS_CHOICES = (
        ('P', 'Pending'),
        ('I', 'In Progress'),
        ('C', 'Completed'),
    )


class User(AbstractUser):
    mobile = models.CharField(max_length=15, blank=True, null=True)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=1, choices=TASK_TYPES, default='O')
    completed_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    assigned_users = models.ManyToManyField(User, related_name='tasks')
    
    def __str__(self):
        return self.name
    
    verbose_name_plural = 'Task'