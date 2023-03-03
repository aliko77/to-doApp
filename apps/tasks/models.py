from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserTasks(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    state = models.CharField(max_length=32)
    expiration_date = models.DateField(null=True)
    is_important = models.BooleanField(default=False)
    step_id = models.BigIntegerField(default=0)
    categories_id = models.BigIntegerField(default=0)
    files_id = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Görev: " + self.title

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Hedef"
        verbose_name_plural = "Hedefler"
