from django.views import View
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest, JsonResponse
from .models import UserTasks
import datetime

# Create your views here.


def is_ajax(request):
    """
    İstek, bir ajax isteği mi?
    """
    return request.headers.get("X-Requested-With") == "XMLHttpRequest"


class Today(LoginRequiredMixin, ListView):
    model = UserTasks
    context_object_name = "user_tasks"
    template_name = "tasks/today.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_tasks"] = self.model.objects.filter(
            author=self.request.user)

        return context


class TaskCreate(LoginRequiredMixin, View):
    def post(self, request):
        if is_ajax(request):
            if not request.POST.get("title"):
                return HttpResponseBadRequest("Eksik data. (title)")

            try:
                exp_date = datetime.datetime.strptime(
                    request.POST.get("expiration_date"), "%d-%m-%Y").date()
            except ValueError:
                exp_date = None

            try:
                ut = UserTasks(
                    author=request.user,
                    title=request.POST.get("title"),
                    expiration_date=exp_date
                )
                ut.save()
                return JsonResponse({"status": True}, status=201)
            except:
                return JsonResponse({"status": False}, status=200)
        else:
            return HttpResponseBadRequest("Bilinmeyen istek")
