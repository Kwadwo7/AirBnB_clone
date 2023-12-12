#!/usr/bin/python3
"""Creates the class State."""

from models.base_model import BaseModel


class State(BaseModel):
    """Inherits from the Basemodel and adds another
    parameter called name
    """

    name = " "
