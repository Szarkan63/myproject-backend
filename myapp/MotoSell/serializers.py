# myapp/serializers.py
from rest_framework import serializers
from .models import Vehicle  # Import the Vehicle model

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'  # Include all fields from the Vehicle model

