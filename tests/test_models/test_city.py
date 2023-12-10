#!/usr/bin/python3
"""Defines unittests for models/city.py."""

import unittest
from models.city import City
from models import storage


class TestCity(unittest.TestCase):
    """Unittests for testing the City class."""

    def test_attributes(self):
        mymodel = City()
        obj = storage.all()[f'City.{mymodel.id}']
        self.assertIn(f'City.{mymodel.id}', storage.all().keys())
        self.assertIn('state_id', obj.__str__())
        self.assertIn('name', obj.__str__())

    def test_type_of_object(self):
        mymodel = City()
        self.assertEqual(City, type(mymodel))
