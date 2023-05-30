# GET /labels/ — страница со списком всех меток
# GET /labels/create/ — страница создания метки
# POST /labels/create/ — создание новой метки
# GET /labels/<int:pk>/update/ — страница редактирования метки
# POST /labels/<int:pk>/update/ — обновление метки
# GET /labels/<int:pk>/delete/ — страница удаления метки
# POST /labels/<int:pk>/delete/ — удаление метки

from django.urls import path as p
from task_manager.views import HomePageView


urlpatterns = [
    p('', HomePageView.as_view()),
]
