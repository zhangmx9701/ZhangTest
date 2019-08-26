from django.db import models

class Ems(models.Model):
    name = models.CharField(max_length=20)
    salary = models.FloatField()
    age = models.SmallIntegerField()
    headpic = models.ImageField(upload_to="pics",null=True)