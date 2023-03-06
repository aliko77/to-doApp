from django.views import View
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest, JsonResponse
from .models import UserTasks
from datetime import datetime

# Create your views here.


def is_ajax(request):
    """
    İstek, bir ajax isteği mi?
    """
    return request.headers.get("X-Requested-With") == "XMLHttpRequest"


def strToDate(str):
    """
    string to date
    @return:
        date,
        except ValueError return None
    """
    try:
        return datetime.strptime(str, "%d-%m-%Y").date()
    except ValueError:
        return None


class Today(LoginRequiredMixin, ListView):
    model = UserTasks
    context_object_name = "user_tasks"
    template_name = "tasks/today.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_tasks"] = self.model.objects.filter(
            author=self.request.user,
            created_at__lte=datetime.today()
        ).order_by("-id")
        return context


class TaskCreate(LoginRequiredMixin, View):
    def post(self, request):
        if is_ajax(request):
            if request.POST.get("title") == None or request.POST.get("expiration_date") == None:
                return HttpResponseBadRequest("Eksik data.")

            try:
                ut = UserTasks(
                    author=request.user,
                    title=request.POST.get("title"),
                    expiration_date=strToDate(
                        request.POST.get("expiration_date"))
                )
                ut.save()
                return JsonResponse({"status": True}, status=201)
            except:
                return JsonResponse({"status": False}, status=200)
        else:
            return HttpResponseBadRequest("Bilinmeyen istek")
