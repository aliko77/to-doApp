from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest, JsonResponse
from .models import UserTasks

# Create your views here.


class Today(LoginRequiredMixin, ListView):
    login_url = "login"

    model = UserTasks
    context_object_name = "user_tasks"
    template_name = "tasks/today.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_tasks"] = self.model.objects.filter(
            author=self.request.user)

        return context


class TaskCreate(LoginRequiredMixin, View):
    login_url = "login"

    def post(self, request):
        is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
        if is_ajax:
            if not request.POST["title"]:
                return HttpResponseBadRequest("Eksik data. (title)")
            ut = UserTasks(
                title=request.POST["title"],
            )
            return JsonResponse({"status": True}, status=200)
        else:
            return HttpResponseBadRequest("Bilinmeyen istek")
