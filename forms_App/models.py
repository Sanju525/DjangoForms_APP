from django.db import models


# Create your models here.


class UserLogs(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.username
