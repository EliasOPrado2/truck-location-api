from django.db import models


class Address(models.Model):
    """
    Model to create Address that will be set into Route as origin and destination.

    :param models (module): hold fields and params to be used into models.
    """

    address = models.CharField(max_length=512, blank=True)
    neighborhood = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=256, blank=True)
    state = models.CharField(max_length=120, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=30, blank=True)
    latitude = models.DecimalField(
        max_digits=22, decimal_places=16, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=22, decimal_places=16, null=True, blank=True
    )

    def __str__(self):
        return str(self.address)
