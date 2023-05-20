from django.urls import path as p
from .views import UsersView


urlpatterns = [
    p('', UsersView.as_view()),
    p('create/', UsersView.as_view()),
    p('<int:pk>/update/', UsersView.as_view()),
    p('<int:pk>/delete/', UsersView.as_view()),
]
