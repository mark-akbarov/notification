from django.db import models
from client.models import Tag, MobileCode


class Notification(models.Model):
    text = models.TextField()
    tag = models.ManyToManyField(Tag)
    mobile_code = models.ManyToManyField(MobileCode)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()