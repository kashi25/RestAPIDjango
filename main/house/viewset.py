from rest_framework import viewsets
from .models import House
from .serializers import HomeSerializer
from .permission import IsHouseManagerOrNone

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    permission_classes = [IsHouseManagerOrNone]
    serializer_call = HomeSerializer