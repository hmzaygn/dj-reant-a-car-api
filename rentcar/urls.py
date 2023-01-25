from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    CarView,
    CustomerView,
    ReservationView
)

router = DefaultRouter()
router.register("cars", CarView)
router.register("customers", CustomerView)
router.register("reservations", ReservationView)


urlpatterns = []

urlpatterns += router.urls
