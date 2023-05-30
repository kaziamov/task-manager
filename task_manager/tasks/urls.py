# GET /tasks/ — страница со списком всех задач
# GET /tasks/create/ — страница создания задачи
# POST /tasks/create/ — создание новой задачи
# GET /tasks/<int:pk>/update/ — страница редактирования задачи
# POST /tasks/<int:pk>/update/ — обновление задачи
# GET /tasks/<int:pk>/delete/ — страница удаления задачи
# POST /tasks/<int:pk>/delete/ — удаление задачи
# GET /tasks/<int:pk>/ — страница просмотра задачи

from django.urls import path as p
from task_manager.views import HomePageView


urlpatterns = [
    p('', HomePageView.as_view()),
]
