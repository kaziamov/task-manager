from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from task_manager.views import BaseFormView, BaseListView

from .models import StatusModel
from .forms import NewStatusForm


class StatusView:
    model = StatusModel


class StatusesListView(StatusView, BaseListView):
    extra_context = {
        'url': reverse_lazy('status_create'),
        'create_url': 'status_create',
        'update_url': 'status_update',
        'delete_url': 'status_delete'
    }


class StatusCreateView(CreateView, BaseFormView):
    form_class = NewStatusForm
    success_url = reverse_lazy('statuses_list')


class StatusUpdateView(StatusView, FormView):
    pass


class StatusDeleteView(StatusView, FormView):
    pass