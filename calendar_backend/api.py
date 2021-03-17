from rest_framework import generics, permissions, viewsets
from .models import Appointment
from .serializer import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = AppointmentSerializer
