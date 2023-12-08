#!/usr/bin/python3
"""Creates class City that reps a real world city"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class City inherits from class Basemodel and has
    2 class attributes.
    """

    def __init__(self, *args, **kwargs):
        """Initializes the class attributes, and the
        inherited ones by calling the super and
        __init__ methods."""

        super().__init__()
        self.state_id = " "
        self.name = " "
