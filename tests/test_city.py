#!/usr/bin/python3obj
"""Unittest for City class"""
import unittest
from models.city import City
from datetime import datetime
from models import storage
import os


class test_city(unittest.TestCase):
    """Test cases for City class"""

    def test_01_init_(self):
        """Test _init_ method"""
        all_objs = storage.all()
        nb_obj = len(all_objs)
        obj = City()
        self.assertIsInstance(obj, City)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertIsInstance(obj.id, str)
        self.assertTrue(len(all_objs) == nb_obj + 1)

        obj = City()
        obj = City()
        obj = City()
        self.assertTrue(len(all_objs) == nb_obj + 4)

        obj.name = "Holberton"
        obj.my_number = 89
        self.assertIsInstance(obj.name, str)
        self.assertIsInstance(obj.my_number, int)

        my_model_json = obj.to_dict()
        my_new_obj = City(**my_model_json)
        self.assertIsInstance(my_new_obj, City)
        self.assertTrue(my_new_obj is not obj)
        self.assertTrue(my_new_obj.created_at == obj.created_at)

        my_model_json["updated_at"] = 'toto'
        my_new_obj1 = City(**my_model_json)
        self.assertIsInstance(my_new_obj1.updated_at, datetime)

    def test_02__str__(self):
        """Test __str__ method"""
        obj = City()
        expected_str = "[City] ({}) {}".format(obj.id, obj.__dict__)
        self.assertTrue(str(obj) == expected_str)

    def test_03_save(self):
        """Test for save method"""
        if os.path.exists('file.json'):
            os.remove('file.json')
        obj = City()
        old_updated_at = obj.updated_at
        self.assertEqual(obj.created_at, obj.updated_at)

        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)
        self.assertTrue(obj.updated_at != old_updated_at)
        self.assertTrue(os.path.exists('file.json'))

    def test_04_to_dict(self):
        """Test to_dict method"""
        obj = City()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIsInstance(obj_dict["__class__"], str)
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)
        self.assertEqual(obj_dict["__class__"], "City")
        self.assertTrue(obj_dict["created_at"] == obj.created_at.isoformat())
        self.assertTrue(obj_dict["updated_at"] == obj.updated_at.isoformat())

    def test_05_attrs(self):
        """Test case for 'City' class attributes"""
        obj = City()
        self.assertEqual(obj.name, "")

    def test_06_inheritance(self):
        """Test case for 'City' class inheritance"""
        obj = City()
        self.assertIsInstance(obj, City)
        self.assertTrue(issubclass(type(obj), City))

    def test_07_instance(self):
        """Test case for 'City' class instance"""
        obj = City()
        self.assertIsInstance(obj, City)
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertTrue(hasattr(obj, "state_id"))
        self.assertTrue(hasattr(obj, "name"))
        self.assertFalse(hasattr(obj, "my_number"))
        obj.my_number = 89
        self.assertTrue(hasattr(obj, "my_number"))

    def test_08_docstring(self):
        """Test case for 'City' class docstring"""
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.__init__.__doc__)
        self.assertIsNotNone(City.__str__.__doc__)
        self.assertIsNotNone(City.save.__doc__)
        self.assertIsNotNone(City.to_dict.__doc__)


if __name__ == "__main__":
    unittest.main()
