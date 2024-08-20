from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # Sprawdź, czy żądanie dotyczy widoku dla ogłoszeń użytkownika
        user_id = self.request.query_params.get('user')
        if user_id is not None:
            return Vehicle.objects.filter(user_id=user_id)
        # W przeciwnym razie zwróć wszystkie ogłoszenia
        return Vehicle.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def delete(self, request, pk, format=None):
        try:
            vehicle = Vehicle.objects.get(pk=pk, user=request.user)
        except Vehicle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({
                'token': access_token,
                'userName': user.username,
                'id': user.id  # Ensure ID is included and is an integer
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

