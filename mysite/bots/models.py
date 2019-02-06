from django.db import models


class Botsdetection(models.Model):
    date = models.DateField()
    users = models.IntegerField(null=True)
    session_count=models.IntegerField(null=True)
