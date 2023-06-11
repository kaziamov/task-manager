from django.contrib import admin
from django.views.i18n import set_language
from django.urls import path, include
from .views import HomePageView
from .users.views import LoginView, LogoutView


urlpatterns = [
    path('', HomePageView.as_view()),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('labels/', include('task_manager.labels.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('i18n/', set_language, name='set_language'),
]
