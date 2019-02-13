from django.db import models


class Botsdetection(models.Model):
    date = models.IntegerField()
    users = models.IntegerField(null=True)
    sessions = models.IntegerField(null=True)
    sessions_per_user = models.IntegerField()
