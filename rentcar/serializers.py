from rest_framework import serializers

from .models import (
    Car,
    Customer,
    Reservation,
)

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = (
            "id",
            "plate_number",
            "brand",
            "model",
            "year",
            "gear",
            "rent_per_day",
            "availability",
        )

class CustomerSerializer(serializers.ModelSerializer):

    user_id = serializers.IntegerField()

    class Meta:
        model = Customer
        fields = (
            "user_id",
            "phone_number",
            "create_date",
            "update_date",
        )

class ReservationSerializer(serializers.ModelSerializer):

    car_id = serializers.IntegerField()
    customer_id = serializers.IntegerField()


    class Meta:
        model = Reservation
        fields = (
            "start_date",
            "end_date",
            "car_id",
            "customer_id",
        )

