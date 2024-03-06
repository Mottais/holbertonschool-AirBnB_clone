#!/usr/bin/python3obj
"""Unittest for Amenity class"""
import unittest
from models.amenity import Amenity
from datetime import datetime
from models import storage
import os


class test_amenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_01_init_(self):
        """Test _init_ method"""
        all_objs = storage.all()
        nb_obj = len(all_objs)
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertIsInstance(obj.id, str)
        self.assertTrue(len(all_objs) == nb_obj + 1)

        obj = Amenity()
        obj = Amenity()
        obj = Amenity()
        self.assertTrue(len(all_objs) == nb_obj + 4)

        obj.name = "Holberton"
        obj.my_number = 89
        self.assertIsInstance(obj.name, str)
        self.assertIsInstance(obj.my_number, int)

        my_model_json = obj.to_dict()
        my_new_obj = Amenity(**my_model_json)
        self.assertIsInstance(my_new_obj, Amenity)
        self.assertTrue(my_new_obj is not obj)
        self.assertTrue(my_new_obj.created_at == obj.created_at)

        my_model_json["updated_at"] = 'toto'
        my_new_obj1 = Amenity(**my_model_json)
        self.assertIsInstance(my_new_obj1.updated_at, datetime)

    def test_02__str__(self):
        """Test __str__ method"""
        obj = Amenity()
        expected_str = "[Amenity] ({}) {}".format(obj.id, obj.__dict__)
        self.assertTrue(str(obj) == expected_str)

    def test_03_save(self):
        """Test for save method"""
        if os.path.exists('file.json'):
            os.remove('file.json')
        obj = Amenity()
        old_updated_at = obj.updated_at
        self.assertEqual(obj.created_at, obj.updated_at)

        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)
        self.assertTrue(obj.updated_at != old_updated_at)
        self.assertTrue(os.path.exists('file.json'))

    def test_04_to_dict(self):
        """Test to_dict method"""
        obj = Amenity()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIsInstance(obj_dict["__class__"], str)
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)
        self.assertEqual(obj_dict["__class__"], "Amenity")
        self.assertTrue(obj_dict["created_at"] == obj.created_at.isoformat())
        self.assertTrue(obj_dict["updated_at"] == obj.updated_at.isoformat())

    def test_05_attrs(self):
        """Test case for 'Amenity' class attributes"""
        obj = Amenity()
        self.assertEqual(obj.name, "")

    def test_06_inheritance(self):
        """Test case for 'Amenity' class inheritance"""
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)
        self.assertTrue(issubclass(type(obj), Amenity))

    def test_07_instance(self):
        """Test case for 'Amenity' class instance"""
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertTrue(hasattr(obj, "name"))
        self.assertFalse(hasattr(obj, "my_number"))
        obj.my_number = 89
        self.assertTrue(hasattr(obj, "my_number"))

    def test_08_docstring(self):
        """Test case for 'Amenity' class docstring"""
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)
        self.assertIsNotNone(Amenity.__str__.__doc__)
        self.assertIsNotNone(Amenity.save.__doc__)
        self.assertIsNotNone(Amenity.to_dict.__doc__)


if __name__ == "__main__":
    unittest.main()
