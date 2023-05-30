# GET /statuses/ — страница со списком всех статусов
# GET /statuses/create/ — страница создания статуса
# POST /statuses/create/ — создание нового статуса
# GET /statuses/<int:pk>/update/ — страница редактирования статуса
# POST /statuses/<int:pk>/update/ — обновление статуса
# GET /statuses/<int:pk>/delete/ — страница удаления статуса
# POST /statuses/<int:pk>/delete/ — удаление статуса

from django.urls import path as p
from task_manager.views import HomePageView


urlpatterns = [
    p('', HomePageView.as_view()),
]
