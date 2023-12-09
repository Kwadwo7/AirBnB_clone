#!/usr/bin/python3
"""Defines the class BaseModel"""

import uuid
import datetime
from models import storage
import time

class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self,*args,**kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if len(kwargs)!=0:
            for i,j in kwargs.items():
                if i != '__class__':
                    if i =='created_at' or i=='updated_at':
                        d_time_obj=datetime.datetime.fromisoformat(j)
                        setattr(self,i,d_time_obj)
                    else:
                        setattr(self,i,j)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)


    def __str__(self):
        """Return the str representation of the BaseModel instance."""
        return f'{[self.__class__.__name__]} ({self.id}) {self.__dict__}'

    def save(self):
        """Update updated_at with the current datetime."""
        time.sleep(0.0001)
        updated_at=datetime.datetime.now()
        storage.save()


        
    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        dict_Format={}
        dict_Format['__class__']=self.__class__.__name__
        for i,j in self.__dict__.items():
            if i == 'created_at' or i == 'updated_at':
                dict_Format[i]=j.isoformat()
            else:
                dict_Format[i]=j
        return dict_Format
