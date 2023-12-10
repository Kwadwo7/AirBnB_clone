#!/usr/bin/python3
"""Defines unittests for console.py."""

from models.base_model import BaseModel
import unittest
from models import storage
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import sys


class TestConsole(unittest.TestCase):
    """Unittests for testing the HBNB command interpreter."""

    def test_prompt(self):
        prompt = '(hbnb) '
        self.assertEqual(prompt, HBNBCommand.prompt)

    def test_quit(self):
        self.assertTrue(HBNBCommand().onecmd('quit'))

    def test_create(self):
        correct = '** class name is missing **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('create'))
            self.assertEqual(correct, output.getvalue().strip())
        correct_1 = "** class name doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('create Model'))
            self.assertEqual(correct_1, output.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('create BaseModel'))
            test_id = f'BaseModel.{output.getvalue().strip()}'
            self.assertIn(test_id, storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('create User'))
            test_id = f'User.{output.getvalue().strip()}'
            self.assertIn(test_id, storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('create Amenity'))
            test_id = f'Amenity.{output.getvalue().strip()}'
            self.assertIn(test_id, storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('create City'))
            test_id = f'City.{output.getvalue().strip()}'
            self.assertIn(test_id, storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('create Place'))
            test_id = f'Place.{output.getvalue().strip()}'
            self.assertIn(test_id, storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('create State'))
            test_id = f'State.{output.getvalue().strip()}'
            self.assertIn(test_id, storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('create Review'))
            test_id = f'Review.{output.getvalue().strip()}'
            self.assertIn(test_id, storage.all().keys())

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('create BaseModel'))
            test_id = output.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as output:
            show_model = f'show BaseModel {test_id}'
            obj = storage.all()[f'BaseModel.{test_id}']
            self.assertFalse(HBNBCommand().onecmd(show_model))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        error_1 = '** class name missing **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('show'))
            self.assertEqual(error_1, output.getvalue().strip())
        error_2 = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('show mymodel'))
            self.assertEqual(error_2, output.getvalue().strip())
        error_3 = '** instance id is missing **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('show BaseModel'))
            self.assertEqual(error_3, output.getvalue().strip())
        error_4 = '** no instance found **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('show BaseModel 1234'))
            self.assertEqual(error_4, output.getvalue().strip())

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('create BaseModel'))
            test_id = output.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as output:
            command = f'show BaseModel {test_id}'
            obj = storage.all()[f'BaseModel.{test_id}']
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as output:
            command_1 = f'destroy BaseModel {test_id}'
            self.assertFalse(HBNBCommand().onecmd(command_1))
        error = '** no instance found **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(error, output.getvalue().strip())
        error_1 = '** class name missing **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('destroy'))
            self.assertEqual(error_1, output.getvalue().strip())
        error_2 = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('destroy mymodel'))
            self.assertEqual(error_2, output.getvalue().strip())
        error_3 = '** instance id is missing **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('destroy BaseModel'))
            self.assertEqual(error_3, output.getvalue().strip())

    def test_all(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('all User'))
            self.assertIn('User', output.getvalue().strip())
            self.assertNotIn('City', output.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('all Place'))
            self.assertIn('Place', output.getvalue().strip())
            self.assertNotIn('City', output.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('all City'))
            self.assertIn('City', output.getvalue().strip())
            self.assertNotIn('Place', output.getvalue().strip())
        error_1 = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('all mymodel'))
            self.assertEqual(error_1, output.getvalue().strip())

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('create BaseModel'))
            test_id = output.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as output:
            command = f'update BaseModel {test_id} name Benedict'
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch('sys.stdout', new=StringIO()) as output:
            command_1 = f'show BaseModel {test_id}'
            self.assertFalse(HBNBCommand().onecmd(command_1))
            self.assertIn('name', output.getvalue().strip())
            self.assertIn('Benedict', output.getvalue().strip())
        error_1 = '** class name missing **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('update'))
            self.assertEqual(error_1, output.getvalue().strip())
        error_2 = "** class name doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('update mymodel'))
            self.assertEqual(error_2, output.getvalue().strip())
        error_3 = '** instance id missing **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('update BaseModel'))
            self.assertEqual(error_3, output.getvalue().strip())
        error_4 = '** no instance found **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('update BaseModel 12345'))
            self.assertEqual(error_4, output.getvalue().strip())
        error_5 = "** attribute name missing **"
        with patch('sys.stdout', new=StringIO()) as output:
            command_2 = f'update BaseModel {test_id}'
            self.assertFalse(HBNBCommand().onecmd(command_2))
            self.assertEqual(error_5, output.getvalue().strip())
        error_6 = '** value missing **'
        with patch('sys.stdout', new=StringIO()) as output:
            command_3 = f'update BaseModel {test_id} name'
            self.assertFalse(HBNBCommand().onecmd(command_3))
            self.assertEqual(error_6, output.getvalue().strip())
