#!/usr/bin/python3
"""Creates the class Review."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review inherits from Basemodel and takes 3
    additional attributes.
    """

    def __init__(self, *args, **kwargs):
        """Initializes the inherited attributes by call
        ing super and __init__ methods, and the 3 class
        attributes."""

        super().__init__()
        self.place_id = " "
        self.user_id = " "
        self.text = " "
