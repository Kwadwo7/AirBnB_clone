#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""

from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
import unittest


class Test_FileStorgae(unittest.TestCase):
    """Unittests for testing the FileStorage class."""
    def setUp(self):
        self.BaseModel_1 = BaseModel()
        storage.save()
        print(self.BaseModel_1)

    def test_FileStorage_new(self):
        new1 = storage.new(self.BaseModel_1)
        self.assertEqual(new1, storage.new(self.BaseModel_1))

    def test_FileStorage_Private_attributes(self):
        self.assertTrue(storage._FileStorage__file_path)
        self.assertTrue(storage._FileStorage__objects)

    def test_FileStorage_all(self):
        self.assertIn(self.BaseModel_1, storage.all().values())

    def test_FileStorage_save(self):
        bm1 = BaseModel()
        storage.save()
        with open('self.__file_path', 'r') as data:
            text = data.read()
        self.assertIn(f'{bm1.__class__.__name__}.{bm1.id}', text)

    def test_FileStorage_reload(self):
        bm1 = BaseModel()
        storage.save()
        with open('self.__file_path') as data:
            obj = f'{bm1.__class__.__name__}.{bm1.id}'
            if obj in data:
                obj2 = storage.reload()
                self.assertEqual(obj2, bm1)
