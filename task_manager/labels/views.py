from django.views.generic import UpdateView, DeleteView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from task_manager.views import BaseFormView, BaseListView
from .models import LabelModel
from .forms import NewLabelForm


class LabelsView:
    model = LabelModel


class LabelsListView(LabelsView, BaseListView):
    extra_context = {
        'url': reverse_lazy('label_create'),
        'create_url': 'label_create',
        'update_url': 'label_update',
        'delete_url': 'label_delete'
    }


class LabelCreateView(CreateView, BaseFormView):
    form_class = NewLabelForm
    success_url = reverse_lazy('labels_list')


class LabelUpdateView(LabelsView, UpdateView):
    pass


class LabelDeleteView(LabelsView, DeleteView):
    pass
