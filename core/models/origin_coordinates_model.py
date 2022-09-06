from django.db import models
from .abstract_models import Coordinates


class OriginCoordinate(Coordinates):
    # add comment
    truck_driver = models.ForeignKey('TruckDriver', on_delete=models.DO_NOTHING)
    destination = models.ForeignKey('DestinationCoordinate', on_delete=models.DO_NOTHING, null=True)