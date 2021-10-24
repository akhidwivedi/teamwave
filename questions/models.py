from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.base import Model
import json



class MainItems(models.Model):
    items = models.JSONField()
    has_more = models.BooleanField()
    backoff  = models.CharField(max_length=5)
    quota_max = models.CharField(max_length=300)
    quota_remaining = models.CharField(max_length=500)

