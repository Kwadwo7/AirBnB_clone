#!/usr/bin/python3
"""A class that inherits from Basemodel"""

from models.base_model import BaseModel
from models import storage


class User(BaseModel):
    """User inherits from the Basemodel and takes
    4 arguments.
    """

    def __init__(self, *args, **kwargs):
        """Initializes attributes inherited from
        Basemodel by caller the super and __init__
        methods"""

        super().__init__()
        self.email = " "
        self.password = " "
        self.first_name = " "
        self.last_name = " "
