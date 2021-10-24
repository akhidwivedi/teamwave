from .models import MainItems
from rest_framework import serializers








class ItemsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MainItems
        fields = "__all__"




