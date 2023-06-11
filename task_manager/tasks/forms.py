from django import forms as f
from .models import TaskModel


class NewTaskForm(f.ModelForm):

    class Meta:
        model = TaskModel
        exclude = ['created_at']
