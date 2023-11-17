
from rest_framework import routers

from .viewsets import UserViewSet, profileViewSet

app_name = "users"

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('profiles', profileViewSet)