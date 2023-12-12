#!/usr/bin/python3
"""Creates class City that reps a real world city"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class City inherits from class Basemodel and has
    2 class attributes.
    """

    state_id = " "
    name = " "
