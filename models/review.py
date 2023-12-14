#!/usr/bin/python3
"""Creates the class Review."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review inherits from Basemodel and takes 3
    additional attributes.
    """
    place_id = ""
    user_id = ""
    text = ""
