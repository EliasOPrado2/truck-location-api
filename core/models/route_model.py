from django.db import models


class Route(models.Model):
    """
    Model to connect origin and destination and connect to truck driver.

    :param models (module): hold fields and params to be used into models.
    """
    truck_driver = models.ForeignKey("TruckDriver", on_delete=models.CASCADE)
    origin = models.ForeignKey(
        "Address", related_name="origin", on_delete=models.CASCADE
    )
    destination = models.ForeignKey(
        "Address", related_name="destination", on_delete=models.CASCADE
    )

    distance = models.IntegerField(null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"route: ${self.id}"
