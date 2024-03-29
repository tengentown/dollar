from django.db import models
import datetime


class Subscriber(models.Model):
    email = models.EmailField()
    creation_date = models.DateTimeField(default=datetime.datetime.now())
