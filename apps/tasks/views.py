from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserTasks

# Create your views here.


class Today(LoginRequiredMixin, ListView):
    login_url = 'login'

    model = UserTasks
    context_object_name = 'user_tasks'
    template_name = "tasks/today.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_tasks'] = self.model.objects.filter(
            author=self.request.user)

        return context
