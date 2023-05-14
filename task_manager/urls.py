from django.contrib import admin
from django.views.i18n import set_language
from django.urls import path
from task_manager.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view()),
    path('i18n/', set_language, name='set_language'),
]
