from rest_framework.viewsets import ModelViewSet

from .models import (
    Car,
    Customer,
    Reservation,
)
from .serializers import (
    CarSerializer,
    CustomerSerializer,
    ReservationSerializer
)

class CarView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CustomerView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CarSerializer

class ReservationView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = CarSerializer


