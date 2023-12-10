#!/usr/bin/python3
"""Defines unittests for models/user.py."""

import unittest
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """Unittests for testing the User class."""

    def test_attributes(self):
        mymodel = User()
        obj = storage.all()[f'User.{mymodel.id}']
        self.assertIn(f'User.{mymodel.id}', storage.all().keys())
        self.assertIn('email', obj.__str__())
        self.assertIn('password', obj.__str__())
        self.assertIn('first_name', obj.__str__())
        self.assertIn('last_name', obj.__str__())

    def test_type_of_object(self):
        mymodel = User()
        self.assertEqual(User, type(mymodel))
