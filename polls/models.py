from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

class Poll(models.Model):
    name = models.CharField(max_length=200, null=True)
    customer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    slug = models.CharField(max_length=100,unique=True)
    guid = models.UUIDField(default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)

class Option(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.PROTECT)
    value = models.CharField(max_length=200, null=True)
    guid = models.UUIDField(default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.PROTECT)
    option = models.ForeignKey(Option, on_delete=models.PROTECT)
    customer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    guid = models.UUIDField(default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
