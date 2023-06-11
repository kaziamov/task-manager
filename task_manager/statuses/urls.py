# GET /statuses/ — страница со списком всех статусов
# GET /statuses/create/ — страница создания статуса
# POST /statuses/create/ — создание нового статуса
# GET /statuses/<int:pk>/update/ — страница редактирования статуса
# POST /statuses/<int:pk>/update/ — обновление статуса
# GET /statuses/<int:pk>/delete/ — страница удаления статуса
# POST /statuses/<int:pk>/delete/ — удаление статуса

from django.urls import path as p

from .views import StatusesListView, StatusCreateView, StatusUpdateView, StatusDeleteView


urlpatterns = [
    p('', StatusesListView.as_view(), name='statuses_list'),
    p('create/', StatusCreateView.as_view(), name='status_create'),
    p('<int:pk>/update', StatusUpdateView.as_view(), name='status_update'),
    p('<int:pk>/delete', StatusDeleteView.as_view(), name='status_delete'),
]
