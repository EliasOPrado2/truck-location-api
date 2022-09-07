from django.urls import include, path
from rest_framework_nested import routers

from core.api.viewsets import (
    AddressViewSet,
    RouteListViewSet,
    RouteViewSet,
    TerminalViewSet,
    TruckDriverViewSet,
)

app_name = "core"

router = routers.DefaultRouter()

router.register(r"truck-drivers", TruckDriverViewSet, basename="truck-drivers")
router.register(r"addresses", AddressViewSet, basename="addresses")
router.register(r"routes", RouteListViewSet, basename="routes")

route_routers = routers.NestedSimpleRouter(
    router, r"truck-drivers", lookup="truckdrivers"
)

route_routers.register(r"routes", RouteViewSet, basename="routes")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(route_routers.urls)),
    path("terminal/", TerminalViewSet.as_view()),
]
