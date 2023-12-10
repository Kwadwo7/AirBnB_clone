#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""

import unittest
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    """Unittests for testing the Amenity class."""

    def test_attributes(self):
        mymodel = Amenity()
        obj = storage.all()[f'Amenity.{mymodel.id}']
        self.assertIn(f'Amenity.{mymodel.id}', storage.all().keys())
        self.assertIn('name', obj.__str__())

    def test_type_of_object(self):
        mymodel = Amenity()
        self.assertEqual(Amenity, type(mymodel))
