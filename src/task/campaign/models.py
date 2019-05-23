import datetime
from django.db import models


# Create your models here.

class Campaign(models.Model):
    url = models.TextField(max_length=300, null=False, blank=False)
    name = models.TextField(max_length=120, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    budget = models.IntegerField()
    goal = models.CharField(max_length=50, null=False, blank=False)
    category = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateField(auto_now=True)
