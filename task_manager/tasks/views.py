from django.views.generic import UpdateView, DeleteView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from task_manager.views import BaseFormView, BaseListView
from .models import TaskModel
from .forms import NewTaskForm


class TaskView:
    model = TaskModel


class TasksListView(TaskView, BaseListView):
    extra_context = {
        'url': reverse_lazy('task_create'),
        'create_url': 'task_create',
        'update_url': 'task_update',
        'delete_url': 'task_delete'
    }


class TaskCreateView(CreateView, BaseFormView):
    form_class = NewTaskForm
    success_url = reverse_lazy('task_create')


class TaskUpdateView(TaskView, UpdateView):
    pass


class TaskDeleteView(TaskView, DeleteView):
    pass
