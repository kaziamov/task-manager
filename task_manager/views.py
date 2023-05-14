from typing import Any, Dict
from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = _('HelloMsg')
        return context
