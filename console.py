#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
        __all_classes: all the user defined classes.
    """
    prompt = "(hbnb) "
    __all_classes = {'BaseModel': BaseModel,
                     'User': User,
                     'Place': Place,
                     'City': City,
                     'State': State,
                     'Amenity': Amenity,
                     'Review': Review}

    def do_quit(self, line):
        """Command to quit the program"""
        return True

    def do_EOF(self, line):
        """EOF signal to quit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing when an empty line is received"""
        pass

    def do_create(self, line):
        """Create a new class instance and print its id."""
        if line in HBNBCommand.__all_classes.keys():
            cls_obj = HBNBCommand.__all_classes[line]
            obj_instance = cls_obj()
            storage.save()
            print(obj_instance.id)
        elif not line:
            print(f'** class name missing **')
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Display the string representation of a
        class instance of a given id.
        """
        file_1 = storage.all()
        if line:
            line = line.split(' ')
            if line[0] not in HBNBCommand.__all_classes:
                print("** class doesn't exist **")
            elif len(line) == 1:
                print("** instance id missing **")
            elif f"{line[0]}.{line[1]}" not in file_1:
                print("** no instance found **")
            else:
                print(file_1[f"{line[0]}.{line[1]}"])
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Delete a class instance of a given id."""
        file_1 = storage.all()
        if line:
            line = line.split(' ')
            if line[0] not in HBNBCommand.__all_classes:
                print("** class doesn't exist **")
            elif len(line) == 1:
                print("** instance id missing **")
            elif f"{line[0]}.{line[1]}" not in file_1:
                print("** no instance found **")
            else:
                del file_1[f"{line[0]}.{line[1]}"]
                storage.save()
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        file_1 = storage.all()
        objL = []
        if line:
            line = line.split(' ')
            if len(line) > 0 and line[0] not in HBNBCommand.__all_classes:
                print("** class doesn't exist **")
            else:
                for obj in file_1.values():
                    if len(line) > 0 and line[0] == obj.__class__.__name__:
                        objL.append(obj.__str__())
                print(objL)
        else:
            for obj in file_1.values():
                objL.append(obj.__str__())
            print(objL)

    def do_update(self, line):
        """Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        file_1 = storage.all()
        if line:
            line = line.split(' ')
            if line[0] not in HBNBCommand.__all_classes:
                print("** class doesn't exist **")
            elif len(line) == 1:
                print('** instance id missing **')
            elif f"{line[0]}.{line[1]}" not in file_1:
                print("** no instance found **")
            elif len(line) == 2:
                print("** attribute name missing **")
            elif len(line) == 3:
                print("** value missing **")
            else:
                objL = file_1[f"{line[0]}.{line[1]}"]
                if line[2] in objL.__class__.__dict__.keys():
                    val_type = type(objL.__class__.__dict__[line[2]])
                    objL.__dict__[line[2]] = val_type(line[3])
                    storage.save()
                else:
                    objL.__dict__[line[2]] = line[3]
                    storage.save()
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
