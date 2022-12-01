import pytz  
from django.db import models


TIMEZONES = (
    zip(pytz.all_timezones, pytz.all_timezones)
)

    
class Tag(models.Model):
    name = models.CharField(max_length=100)


class MobileCode(models.Model):
    code = models.CharField(max_length=5)
    


class Client(models.Model):
    phone_number = models.CharField(max_length=10)
    mobile_code = models.ForeignKey(MobileCode, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    time_zone = models.CharField(max_length=100, choices=TIMEZONES) 