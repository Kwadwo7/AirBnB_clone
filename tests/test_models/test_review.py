#!/usr/bin/python3
"""Defines unittests for models/review.py."""

import unittest
from models.review import Review
from models import storage

class TestReview(unittest.TestCase):
    """Unittests for testing the Review class."""

    def test_attributes(self):
        mymodel=Review()
        obj=storage.all()[f'Review.{mymodel.id}']
        self.assertIn(f'Review.{mymodel.id}',storage.all().keys())
        self.assertIn('place_id',obj.__str__())
        self.assertIn('user_id', obj.__str__())
        self.assertIn('text', obj.__str__())

    def test_type_of_object(self):
        mymodel=Review()
        self.assertEqual(Review,type(mymodel))
