#!/usr/bin/python3
"""Creates class Amenity reps the amenity available."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Inherits from class Basemodel and has one class
    attribute.
    """

    def __init__(self, *args, **kwargs):
        """Initializes the name attribute, and the
        inherited ones by calling the super and
        __init__ methods."""

        super().__init__()
        self.name = " "
