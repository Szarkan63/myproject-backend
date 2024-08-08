
from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all() #Okresla ktore obiekty beda modyfikowane
    serializer_class = VehicleSerializer  #Mówi jak przekstalcic obiekty modelu na JSON
