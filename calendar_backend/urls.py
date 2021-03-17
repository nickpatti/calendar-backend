from django.urls import path
from .api import AppointmentViewSet
from knox import views as knox_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/appointment', AppointmentViewSet, 'appointment')
