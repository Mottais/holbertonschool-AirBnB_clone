#!/usr/bin/python3
"""Unittest for class BaseModel"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class test_Basemodel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_01_init_(self):
        """Test _init_ method"""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)
        self.assertIsInstance(base.id, str)

        base.name = "Holberton"
        base.my_number = 89
        self.assertIsInstance(base.name, str)
        self.assertIsInstance(base.my_number, int)

    def test_02__str__(self):
        """Test __str__ method"""
        base = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(base.id, base.__dict__)
        self.assertTrue(str(base) == expected_str)

    def test_03_save(self):
        """Test for save method"""
        base = BaseModel()
        old_updated_at = base.updated_at
        base.save()
        self.assertTrue(base.updated_at != old_updated_at)

    def test_04_dict(self):
        """Test to_dict method"""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertIsInstance(base_dict["__class__"], str)
        self.assertIsInstance(base_dict["created_at"], str)
        self.assertIsInstance(base_dict["updated_at"], str)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertTrue(base_dict["created_at"] == base.created_at.isoformat())
        self.assertTrue(base_dict["updated_at"] == base.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
