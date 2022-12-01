from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .seriazlizers import *
from .models import *


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    

class MobileCodeViewSet(ModelViewSet):
    serializer_class = MobileCodeSerializer
    queryset = MobileCode.objects.all()
    permission_classes = [IsAuthenticated,]


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated,]