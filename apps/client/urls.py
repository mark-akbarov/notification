from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()

router.register('tag', TagViewSet)
router.register('mobile_code', MobileCodeViewSet)
router.register('client', ClientViewSet)


urlpatterns = router.urls