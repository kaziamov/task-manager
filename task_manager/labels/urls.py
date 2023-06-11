from django.urls import path as p

from .views import LabelsListView, LabelCreateView, LabelUpdateView, LabelDeleteView


urlpatterns = [
    p('', LabelsListView.as_view(), name='labels_list'),
    p('create/', LabelCreateView.as_view(), name='label_create'),
    p('<int:pk>/update', LabelUpdateView.as_view(), name='label_update'),
    p('<int:pk>/delete', LabelDeleteView.as_view(), name='label_delete'),
]
