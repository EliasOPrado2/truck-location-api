from rest_framework import viewsets

from core.api.serializers import RouteSerializer
from core.models import Route


class RouteViewSet(viewsets.ModelViewSet):
    """
    View to display Route nested into the truck-drivers endpoint. 
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def get_queryset(self):
        truck_driver_id = self.kwargs["truckdrivers_pk"]
        return Route.objects.filter(truck_driver=truck_driver_id)


class RouteListViewSet(viewsets.ModelViewSet):
    """
    View to display on its own endpoit with get only available.
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    http_method_names = ["get"]
