#!/usr/bin/python3
"""Creates class Place that represents a real palce."""

from models.base_model import BaseModel


class Place(BaseModel):
    """Inherits from class Basemodel and takes args and
    kwargs.
    """

    def __init__(self, *args, **kwargs):
        """Initializes class attributes, and the
        inherited ones by calling super and __init__
        methods."""

        super().__init__()
        self.city_id = " "
        self.user_id = " "
        self.name = " "
        self.description = " "
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
