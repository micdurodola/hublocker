from rest_framework import serializers
from .models import Locker


#Locker Model Serializers

class LockerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Locker
        fields = "__all__"

        