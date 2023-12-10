from rest_framework import serializers
from .models import House


class HomeSerializer(serializers.ModelSerializer):
    
    members_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = House
        fields = ['url', 'id', 'image', 'name', 'created_on',
                  'manager', 'description', 'members_count',
                  'members', 'points', 'completed_tasks_count',
                  'notcompleted_tasks_count', 'tasklists']
        read_only_fields = ['points', 'completed_tasks_count','notcompleted_tasks_count']