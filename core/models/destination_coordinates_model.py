from django.db import models
from .abstract_models import Coordinates


class DestinationCoordinate(Coordinates):
    # add comment
    truck_driver = models.ForeignKey('TruckDriver', on_delete=models.DO_NOTHING)
    origin = models.ForeignKey('OriginCoordinate', on_delete=models.DO_NOTHING)