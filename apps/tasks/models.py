from django.db import models

# Create your models here.


class UserTasks(models.Model):
    user_id = models.IntegerField()
    content = models.CharField(max_length=255)
    expiration_date = models.DateField()

    def __str__(self):
        return self.name
