from django.urls import path
from .views import Today, TaskCreate

urlpatterns = [
    path('today/', Today.as_view(), name='tasks.today'),
    path("create/", TaskCreate.as_view(), name="tasks.create")
]
