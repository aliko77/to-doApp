from django.shortcuts import render, redirect
from django.views import View

# Create your views here.


class index(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('tasks.today')
        return render(request=request, template_name='main/index.html')
