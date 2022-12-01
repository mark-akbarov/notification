from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from .serializer import MessageSerializer, ScheduledMessageSerializer
from .models import Message


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated,]
    

class SendScheduledMessageAPIView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        serializer = ScheduledMessageSerializer
        if serializer.is_valid():
            message_id = serializer.validated_data['message_id']
            datetime = serializer.validated_data['datetime']
            message = Message.objects.get(id=message_id)
            