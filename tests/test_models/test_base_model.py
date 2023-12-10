#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""

import datetime
import unittest
from models.base_model import BaseModel


class test_BaseModel(unittest.TestCase):
    """Unittests for testing the BaseModel class."""

    def test_BaseModel_save(self):
        """A test to check if the created_at time is different
           from updated_at time
        """
        BaseModel_1 = BaseModel()
        self.assertNotEqual(BaseModel_1.created_at, BaseModel_1.save())

    def test_BaseModel_to_dict(self):
        """A test to check if all the attributes are present
           in the to_dict function
        """
        BaseModel_1 = BaseModel()
        list_1 = ['id', 'created_at', 'updated_at', '__class__']
        for i in list_1:
            self.assertIn(i, BaseModel_1.to_dict())

    def test_BaseModel_datetimeObject(self):
        BaseModel_1 = BaseModel()
        self.assertEqual(datetime.datetime, type(BaseModel_1.created_at))
        self.assertEqual(datetime.datetime, type(BaseModel_1.updated_at))
        self.assertEqual(str, type((BaseModel_1.id)))

    def test_BaseModel_argsIn_Instance(self):
        l1 = datetime.datetime.now()
        l2 = l1.isoformat()
        test_dict = {'id': '1234567', 'created_at': l2}
        BM_1 = BaseModel()
        BM_2 = BaseModel(**test_dict)
        self.assertEqual(type(BM_1.created_at), type(BM_2.created_at))
