from django.db import models as m
from django.utils import timezone
from task_manager.users.models import UserModel
from task_manager.statuses.models import StatusModel
from task_manager.labels.models import LabelModel


class TaskModel(m.Model):
    name = m.CharField(max_length=255, unique=True)
    desk = m.CharField(max_length=255, blank=True)

    author = m.ForeignKey(UserModel, on_delete=m.PROTECT, related_name='author')
    executor = m.ForeignKey(UserModel, on_delete=m.PROTECT, related_name='executor', blank=True)

    status = m.ForeignKey(StatusModel, on_delete=m.PROTECT, blank=True)
    label = m.ForeignKey(LabelModel, on_delete=m.SET_DEFAULT, default=None)

    created_at = m.DateField(default=timezone.now)
    updated_at = m.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name
