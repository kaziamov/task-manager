# GET /tasks/ — страница со списком всех задач
# GET /tasks/create/ — страница создания задачи
# POST /tasks/create/ — создание новой задачи
# GET /tasks/<int:pk>/update/ — страница редактирования задачи
# POST /tasks/<int:pk>/update/ — обновление задачи
# GET /tasks/<int:pk>/delete/ — страница удаления задачи
# POST /tasks/<int:pk>/delete/ — удаление задачи
# GET /tasks/<int:pk>/ — страница просмотра задачи

from django.urls import path as p

from .views import TaskCreateView, TaskDeleteView, TaskUpdateView, TasksListView


urlpatterns = [
    p('', TasksListView.as_view(), name='tasks_list'),
    p('create/', TaskCreateView.as_view(), name='task_create'),
    p('<int:pk>/update', TaskUpdateView.as_view(), name='task_update'),
    p('<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),
]
