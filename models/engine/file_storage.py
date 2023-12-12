#!/usr/bin/python3
"""Defines the FileStorage class."""
import json


class FileStorage:
    """Represent an abstracted storage engine.

        Attributes:
            __file_path (str): The name of the file to save objects to.
            __objects (dict): A dictionary of instantiated objects.
        """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        serialize_string = {}
        for i, j in FileStorage.__objects.items():
            serialize_string[i] = j.to_dict()
            with open(FileStorage.__file_path, "w", encoding="utf-8") as data:
                json.dump(serialize_string, data)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review

        definedClass = {'BaseModel': BaseModel,
                        'User': User,
                        'Place': Place,
                        'City': City,
                        'State': State,
                        'Amenity': Amenity,
                        'Review': Review
                        }
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as data:
                data_2 = json.load(data)
                for i in data_2.values():
                    data_3 = i["__class__"]
                    class_object = definedClass[data_3]
                    self.new(class_object(**i))
        except FileNotFoundError:
            pass
