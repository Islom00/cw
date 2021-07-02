from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=50, null=False)
    age = models.IntegerField(null=True)
    salary = models.FloatField(null=False)
