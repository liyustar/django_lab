from django import forms

from .models import Dict

class DictForm(forms.ModelForm):
    class Meta:
        model = Dict
        fields = [
            "name",
            "desc",
            "dataType",
        ]
