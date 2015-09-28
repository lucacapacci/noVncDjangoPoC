from django.db import models


class UserHostPort(models.Model):
    username = models.TextField()
    host = models.TextField()
    port = models.IntegerField()