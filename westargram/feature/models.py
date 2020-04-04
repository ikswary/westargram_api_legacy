from django.db import models


class Comments(models.Model):
    username = models.CharField(max_length=50)
    comment = models.CharField(max_length=300)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class UserData(models.Model):
    userid = models.CharField(max_length=20)
    comment = models.CharField(max_length=20)