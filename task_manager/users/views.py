from typing import Any, Dict
from django.views.generic.base import TemplateView


class UsersView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)
