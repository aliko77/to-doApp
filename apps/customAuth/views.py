from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm

# Create your views here.


class Login(View):
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request=request,
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password')
            )
            if user is not None:
                login(request=request, user=user)
                return redirect('tasks.today')
            else:
                messages.error(
                    request=request, message='Email veya şifre yanlış.')
                return redirect('login')
        else:
            messages.error(
                request=request, message='Email veya şifre yanlış.'
            )
        return redirect('login')

    def get(self, request):
        return render(request, 'customAuth/login.html')


class Register(View):
    def post(self, request):
        """
        redirect guest users to home page
        """
        if request.user.is_authenticated:
            return redirect('home')
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request=request, message='Başarıyla kayıt oldunuz.')
            return redirect('login')
        else:
            return render(request, 'customAuth/register.html', {'form': form})

    def get(self, request):
        """
        redirect guest users to home page
        """
        if request.user.is_authenticated:
            return redirect('home')
        return render(request=request, template_name='customAuth/register.html')


class Logout(View):
    def get(self, request):
        logout(request=request)
        return redirect('home')
