#!/usr/bin/python3
"""BaseModel unittest module"""

import os
from uuid import uuid4
import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """basemodel test class"""

    def setUp(self):
        """Setup for temporary file path"""
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Tear down for temporary file path"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        """Test for init"""
        model = BaseModel()

        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_str(self):
        """Test for __str__"""
        model = BaseModel()

        self.assertTrue(str(model).startswith('[BaseModel]'))

        self.assertIn(model.id, str(model))

        self.assertIn(str(model.__dict__), str(model))

    def test_save(self):
        """Test for save method"""
        model = BaseModel()

        init_updated_at = model.updated_at

        current_updated_at = model.save()

        self.assertNotEqual(init_updated_at, current_updated_at)

    def test_to_dict(self):
        """Test for to_dict method"""
        model = BaseModel()

        model_dict = model.to_dict()

        self.assertIsInstance(model_dict, dict)

        self.assertEqual(model_dict["__class__"], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'],
                         model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         model.updated_at.isoformat())
