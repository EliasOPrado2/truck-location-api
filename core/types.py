from django.db import models


class TruckType(models.IntegerChoices):
    VUC_34 = 1, "CARGO 3/4"
    TOCO = 2, "TOCO"
    TRUCK = 3, "TRUCK"
    SIMPLE = 4, "SIMPLE"
    EXTENDED_AXLE = 5, "EXTENDED AXLE"


class CNHType(models.TextChoices):
    # Remember to create a logic that
    # checks types of cnh and truck_type.
    TYPE_C = 1, "C"
    TYPE_D = 2, "D"
    TYPE_E = 3, "E"


class SexType(models.IntegerChoices):
    MALE = 0, "MALE"
    FEMALE = 1, "FEMALE"
    TRANSGENDER = 2, "TRANSGENDER"
    NO_ANWER = 3, "NO ANSWER"