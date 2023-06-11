from typing import Any, Dict
from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView
from django.views.generic import FormView, ListView
from abc import abstractmethod


class HomePageView(TemplateView):
    """Homepage view"""
    template_name = "home.html"


@abstractmethod
class BaseListView(ListView):
    model = None
    template_name = 'list.html'
    extra_content = {}

    @classmethod
    def get_model(cls):
        return cls

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        model = self.get_model().model
        context = super().get_context_data(**kwargs)
        context['fields'] = [field.name for field in model._meta.get_fields()]
        return context


class BaseFormView(FormView):
    template_name = 'form.html'
