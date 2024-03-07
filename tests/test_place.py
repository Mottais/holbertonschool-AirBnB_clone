#!/usr/bin/python3obj
"""Unittest for Place class"""
import unittest
from models.place import Place
from datetime import datetime
from models import storage
import os


class test_place(unittest.TestCase):
    """Test cases for Place class"""

    def test_01_init_(self):
        """Test _init_ method"""
        all_objs = storage.all()
        nb_obj = len(all_objs)
        obj = Place()
        self.assertIsInstance(obj, Place)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertIsInstance(obj.id, str)
        self.assertTrue(len(all_objs) == nb_obj + 1)

        obj = Place()
        obj = Place()
        obj = Place()
        self.assertTrue(len(all_objs) == nb_obj + 4)

        obj.name = "Holberton"
        obj.my_number = 89
        self.assertIsInstance(obj.name, str)
        self.assertIsInstance(obj.my_number, int)

        my_model_json = obj.to_dict()
        my_new_obj = Place(**my_model_json)
        self.assertIsInstance(my_new_obj, Place)
        self.assertTrue(my_new_obj is not obj)
        self.assertTrue(my_new_obj.created_at == obj.created_at)

        my_model_json["updated_at"] = 'toto'
        my_new_obj1 = Place(**my_model_json)
        self.assertIsInstance(my_new_obj1.updated_at, datetime)

    def test_02__str__(self):
        """Test __str__ method"""
        obj = Place()
        expected_str = "[Place] ({}) {}".format(obj.id, obj.__dict__)
        self.assertTrue(str(obj) == expected_str)

    def test_03_save(self):
        """Test for save method"""
        if os.path.exists('file.json'):
            os.remove('file.json')
        obj = Place()
        old_updated_at = obj.updated_at
        self.assertEqual(obj.created_at, obj.updated_at)

        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)
        self.assertTrue(obj.updated_at != old_updated_at)
        self.assertTrue(os.path.exists('file.json'))

    def test_04_to_dict(self):
        """Test to_dict method"""
        obj = Place()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIsInstance(obj_dict["__class__"], str)
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)
        self.assertEqual(obj_dict["__class__"], "Place")
        self.assertTrue(obj_dict["created_at"] == obj.created_at.isoformat())
        self.assertTrue(obj_dict["updated_at"] == obj.updated_at.isoformat())

    def test_05_attrs(self):
        """Test case for 'Place' class attributes"""
        obj = Place()
        self.assertEqual(obj.user_id, "")

    def test_06_inheritance(self):
        """Test case for 'Place' class inheritance"""
        obj = Place()
        self.assertIsInstance(obj, Place)
        self.assertTrue(issubclass(type(obj), Place))

    def test_07_instance(self):
        """Test case for 'Place' class instance"""
        obj = Place()
        self.assertIsInstance(obj, Place)
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertTrue(hasattr(obj, "city_id"))
        self.assertTrue(hasattr(obj, "user_id"))
        self.assertTrue(hasattr(obj, "name"))
        self.assertTrue(hasattr(obj, "description"))
        self.assertTrue(hasattr(obj, "number_rooms"))
        self.assertTrue(hasattr(obj, "number_bathrooms"))
        self.assertTrue(hasattr(obj, "max_guest"))
        self.assertTrue(hasattr(obj, "price_by_night"))
        self.assertTrue(hasattr(obj, "latitude"))
        self.assertTrue(hasattr(obj, "longitude"))
        self.assertTrue(hasattr(obj, "amenity_ids"))
        self.assertFalse(hasattr(obj, "my_number"))
        obj.my_number = 89
        self.assertTrue(hasattr(obj, "my_number"))

    def test_08_docstring(self):
        """Test case for 'Place' class docstring"""
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)
        self.assertIsNotNone(Place.__str__.__doc__)
        self.assertIsNotNone(Place.save.__doc__)
        self.assertIsNotNone(Place.to_dict.__doc__)


if __name__ == "__main__":
    unittest.main()
