from rest_framework import routers
from users.views import UserViewSet
from trips.views import  TripViewSet
from places.views import PlaceViewSet
from vehicles.views import  VehicleViewSet

router = routers.DefaultRouter()

router.register('user',UserViewSet)
router.register('places',PlaceViewSet)
router.register('vehicles',VehicleViewSet)
router.register('trips',TripViewSet)
