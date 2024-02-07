from django import forms

from tasks.models import Tag, Task


class TaskCreateFrom(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "tags"
        ]
        widgets = {
            "tags": forms.CheckboxSelectMultiple,
        }


class TagCreateFrom(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            "name"
        ]
