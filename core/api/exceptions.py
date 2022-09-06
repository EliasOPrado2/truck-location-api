from rest_framework import status
from rest_framework.exceptions import APIException


class InvalidAddress(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = (
        "This address is not valid or does not exist."
    )
    default_code = "invalid"


class NoSimilarAddress(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = (
        "Origin and destination should not be similar."
    )
    default_code = "invalid"

class OriginAlreadyPopulated(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = (
        "The current origin already has a destination."
    )
    default_code = "invalid"