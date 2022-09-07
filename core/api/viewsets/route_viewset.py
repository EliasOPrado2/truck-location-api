from rest_framework import viewsets

from core.api.serializers import RouteSerializer
from core.models import Route


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def get_queryset(self):
        truck_driver_id = self.kwargs["truckdrivers_pk"]
        return Route.objects.filter(truck_driver=truck_driver_id)


class RouteListViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    http_method_names = ["get"]
