from django.urls import path
from . import views

urlpatterns = [
    path('today/', views.Today.as_view(), name='tasks.today')
]
