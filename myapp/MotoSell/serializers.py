# myapp/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['title', 'description', 'category', 'brand', 'model', 'year', 'mileage', 'engine_capacity', 'power',
                  'fuel_type', 'photo']
        extra_kwargs = {
            'user': {'read_only': True},  # user is not editable by the user
            'date_added': {'read_only': True},
            'date_published': {'read_only': True},
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

