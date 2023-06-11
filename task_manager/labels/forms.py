from django import forms as f
from .models import LabelModel


class NewLabelForm(f.ModelForm):

    class Meta:
        model = LabelModel
        exclude = []
