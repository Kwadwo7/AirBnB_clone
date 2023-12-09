#!/usr/bin/python3
"""Defines unittests for models/state.py."""

import unittest
from models.state import State
from models import storage

class TestState(unittest.TestCase):
    """Unittests for testing the State class."""

    def test_attributes(self):
        mymodel=State()
        obj=storage.all()[f'State.{mymodel.id}']
        self.assertIn(f'State.{mymodel.id}',storage.all().keys())
        self.assertIn('name', obj.__str__())

    def test_type_of_object(self):
        mymodel=State()
        self.assertEqual(State,type(mymodel))
