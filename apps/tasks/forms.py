from django import forms
from .models import UserTasks

class TaskCreatePost(forms.ModelForm):
    class Meta:
        model = UserTasks
        fields = ["title"]