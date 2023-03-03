from django.urls import path
from .views import Today

urlpatterns = [
    path('today/', Today.as_view(), name='tasks.today')
]
