from rest_framework import viewsets


class CoordinatesViewSetMixin(viewsets.ModelViewSet):

    def get_queryset(self):
        """
        Display a queryset based on the truckdrivers_id parameter.

        :return queryset: The requested queryset.
        """
        try:
            truck_driver_id = self.kwargs["truckdrivers_pk"]
            if truck_driver_id:
                return self.model.objects.filter(truck_driver_id=truck_driver_id)

        except KeyError as e:
            print(e)
            return self.queryset