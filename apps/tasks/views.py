from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class Today(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        return render(request=request, template_name='tasks/today.html')
