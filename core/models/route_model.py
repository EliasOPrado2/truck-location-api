from django.db import models 


class Route(models.Model):
    """
    Model to connect origin and destination and connect to truck driver.

    :param models (module): hold fields and params to be used into models.
    """
    origin = models.ForeignKey('OriginCoordinate', on_delete=models.DO_NOTHING)
    destination = models.ForeignKey('DestinationCoordinate', on_delete=models.DO_NOTHING)
    distance = models.IntegerField()

    def __str__(self):
        return f"route: ${self.id}"