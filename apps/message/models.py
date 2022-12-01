from django.db import models
from client.models import Client
from notification.models import Notification


MESSAGE_STATUS = (
    ('SUCCESSFULL', 'SUCCESSFULL'),
    ('FAILED', 'FAILED'),
    ('PENDING', 'PENDING')
)


class Message(models.Model):
    date = models.DateTimeField(auto_now=True)
    message_status = models.CharField(max_length=100, choices=MESSAGE_STATUS)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)