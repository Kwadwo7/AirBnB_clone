#!/usr/bin/python3
"""Creates class Amenity reps the amenity available."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Inherits from class Basemodel and has one class
    attribute.
    """

    name = ""
