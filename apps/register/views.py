from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.


class register(View):
    def post(self, request):
        """
        redirect guest users to home page
        """
        if request.user.is_authenticated:
            return redirect('home')
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(
                request=request, message='Başarıyla kayıt oldunuz.')
            return redirect('login')
        else:
            return render(request, 'register/register.html', {'form': form})

    def get(self, request):
        """
        redirect guest users to home page
        """
        if request.user.is_authenticated:
            return redirect('home')
        return render(request=request, template_name='register/register.html')
