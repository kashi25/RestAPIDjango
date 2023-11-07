from django.contrib.auth.models import User

from rest_framework import viewsets

from .serializers import UserSerializer
from .permissions import IsUserOwnerOrGetAndPostOnly

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
