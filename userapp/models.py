from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    sex = models.CharField(max_length=5)
    headpic = models.ImageField(upload_to="user",null=True)