from django.urls import path
from apps.register import views

urlpatterns = [
    path('register/', views.register.as_view(), name='register')
]
