from django.db import models
from core.types import TruckType, CNHType, SexType



class TruckDriver(models.Model):
    # add comment
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    sex = models.IntegerField(blank=True, null=True, choices=SexType.choices)
    has_truck = models.BooleanField(default=False)
    cnh_type = models.IntegerField(choices=CNHType.choices)
    is_loaded = models.BooleanField(default=False)
    truck_type = models.IntegerField(choices=TruckType.choices)
    # origin = models.ForeignKey('OriginCoordinate', on_delete=models.CASCADE)
    # destination = models.ForeignKey('DestinationCoordinate', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)