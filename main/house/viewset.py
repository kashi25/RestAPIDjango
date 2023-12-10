from rest_framework import viewsets
from .models import House
from .serializers import HomeSerializer

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    permission_classes = []
    serializer_call = HomeSerializer