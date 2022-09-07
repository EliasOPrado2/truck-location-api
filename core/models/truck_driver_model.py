from django.db import models

from core.types import CNHType, SexType, TruckType


class TruckDriver(models.Model):
    """
    Model to insert driver's data.

    :param models (module): hold fields and params to be used into models.
    """
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    sex = models.IntegerField(blank=True, null=True, choices=SexType.choices)
    has_truck = models.BooleanField(default=False)
    cnh_type = models.IntegerField(choices=CNHType.choices)
    is_loaded = models.BooleanField(default=False)
    truck_type = models.IntegerField(choices=TruckType.choices)

    def __str__(self):
        return str(self.name)
