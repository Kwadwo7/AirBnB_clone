#!/usr/bin/python3
"""A class that inherits from Basemodel"""

from models.base_model import BaseModel
from models import storage


class User(BaseModel):
    """User inherits from the Basemodel and takes
    4 arguments.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
