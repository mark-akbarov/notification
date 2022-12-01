from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        
        
class ScheduledMessageSerializer(serializers.Serializer):
    message_id = serializers.IntegerField()
    datetime = serializers.DateTimeField()