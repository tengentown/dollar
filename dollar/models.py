from django.db import models
from datetime import datetime


class Subscriber(models.Model):
    email = models.EmailField()
