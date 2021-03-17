from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Customer, Account, Staff, Availability
from math import ceil
from calendar_backend.models import Appointment
# User Serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'email', 'is_staff')

# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'email', 'password', 'date_of_birth')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Account.objects.create_user(validated_data['email'], validated_data['password'], validated_data['date_of_birth'])

        return user

# Login Serializer


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('id', 'email', 'is_staff', 'date_of_birth', 'date_joined', 'last_login')


class AppointmentSlotsField(serializers.RelatedField):
    def get_queryset(self):
        return Appointment.objects.all()

    def to_representation(self, value):
        duration = value.duration / 1800
        return duration


class AvailabilitySerializer(serializers.ModelSerializer):
    time_range = serializers.SerializerMethodField()
    slots = serializers.SerializerMethodField()

    class Meta:
        model = Availability
        fields = ('id', 'start_time', 'end_time', 'time_range', 'slots')

    def get_time_range(self, obj):
        start = obj.start_time
        end = obj.end_time
        step = datetime.timedelta(hours=0.5)
        time_list = []

        while start <= end:
            time_list.append(start)
            start += step

        return time_list

    def get_slots(self, obj):
        return (len(self.get_time_range(obj)))


class StaffSerializer(serializers.ModelSerializer):
    relation = AccountSerializer()
    availability = AvailabilitySerializer(read_only=True, many=True)
    appointment = AppointmentSlotsField(many=True)
    appointment_count = serializers.SerializerMethodField()
    customer = serializers.StringRelatedField(many=True)
    customer_count = serializers.SerializerMethodField()
    available_slots = serializers.SerializerMethodField()

    class Meta:
        model = Staff
        fields = ('id', 'relation', 'name', 'availability', 'customer', 'customer_count', 'appointment_count', 'available_slots', 'appointment')
        depth = 1

    def get_appointment_count(self, obj):
        return obj.appointment_count

    def get_customer_count(self, obj):
        return obj.customer_count

    def get_completed_appointments(self, obj):
        pass

    def get_cancelled_appointments(self, obj):
        pass

    def get_available_slots(self, obj):
        pass
        # take away one slot for every 30 minute appointment, 2 for 60. Using ceil to always round up
        # return int(appointment)


class CustomerSerializer(serializers.ModelSerializer):
    relation = AccountSerializer()
    counsellor = StaffSerializer

    class Meta:
        model = Customer
        fields = '__all__'
