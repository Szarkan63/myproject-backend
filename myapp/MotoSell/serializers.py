# myapp/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Vehicle
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['title', 'description', 'category', 'brand', 'model', 'year', 'mileage', 'engine_capacity', 'power',
                  'fuel_type', 'photo', 'user']
        extra_kwargs = {
            'date_added': {'read_only': True},
            'date_published': {'read_only': True},
        }

    def create(self, validated_data):
        # Ensure user is set in the view, not from the client
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)

    def destroy(self, request, *args, **kwargs):
        # Pobierz obiekt do usunięcia
        vehicle = self.get_object()

        # Sprawdź, czy użytkownik jest właścicielem ogłoszenia
        if vehicle.user != request.user:
            return Response({"detail": "Nie masz uprawnień do usunięcia tego ogłoszenia."},
                            status=status.HTTP_403_FORBIDDEN)

        # Wywołaj metodę destroy z superklasy
        return super().destroy(request, *args, **kwargs)

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

