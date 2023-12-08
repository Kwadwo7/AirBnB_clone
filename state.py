#!/usr/bin/python3
"""Creates the class State."""

from models.base_model import BaseModel


class State(BaseModel):
    """Inherits from the Basemodel and adds another
    parameter called name
    """

    def __init__(self, *args, **kwargs):
        """Initializes the inherited attributes and
        methods by calling super and __init__ methods
        , and the name attribute too."""

        super().__init__()
        self.name = " "
