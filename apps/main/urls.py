from django.urls import path
from apps.main.views import index as indexView

urlpatterns = [
    path('', indexView.as_view(), name='index')
]
