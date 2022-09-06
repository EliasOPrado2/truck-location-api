from rest_framework import viewsets
from core.models import Route
from core.api.serializers import RouteSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def get_queryset(self):
        truck_driver_id = self.kwargs["truckdrivers_pk"]
        return Route.objects.filter(truck_driver=truck_driver_id)
