#!/usr/bin/python3
"""Defines unittests for models/place.py."""

import unittest
from models.place import Place
from models import storage

class TestPlace(unittest.TestCase):
    """Unittests for testing the Place class."""

    def test_attributes(self):
        mymodel=Place()
        obj=storage.all()[f'Place.{mymodel.id}']
        self.assertIn(f'Place.{mymodel.id}',storage.all().keys())
        self.assertIn('city_id',obj.__str__())
        self.assertIn('user_id', obj.__str__())
        self.assertIn('name', obj.__str__())
        self.assertIn('description', obj.__str__())
        self.assertIn('number_rooms', obj.__str__())
        self.assertIn('number_bathrooms', obj.__str__())
        self.assertIn('max_guest', obj.__str__())
        self.assertIn('price_by_night', obj.__str__())
        self.assertIn('latitude', obj.__str__())
        self.assertIn('longitude', obj.__str__())
        self.assertIn('amenity_ids', obj.__str__())

    def test_type_of_object(self):
        mymodel=Place()
        self.assertEqual(Place,type(mymodel))
