from django.urls import path
from apps.register.views import register

urlpatterns = [
    path('register', register.as_view(), name='register')
]
