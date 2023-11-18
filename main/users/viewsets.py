from django.contrib.auth.models import User

from rest_framework import viewsets

from .serializers import UserSerializer, ProfileSerializer
from .permissions import IsUserOwnerOrGetAndPostOnly, IsProfileownerReadOnly
from .models import Profile

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class profileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsProfileownerReadOnly,]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
