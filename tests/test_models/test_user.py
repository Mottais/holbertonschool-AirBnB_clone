#!/usr/bin/python3
"""Unittest for User class"""
import unittest
from datetime import datetime
import os
from models import storage
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class"""
    def test_01_init_(self):
        """Test _init_ method"""
        all_objs = storage.all()
        nb_obj = len(all_objs)
        obj = User()
        self.assertIsInstance(obj, User)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertIsInstance(obj.id, str)
        self.assertTrue(len(all_objs) == nb_obj + 1)

        obj = User()
        obj = User()
        obj = User()
        self.assertTrue(len(all_objs) == nb_obj + 4)

        obj.name = "Holberton"
        obj.my_number = 89
        self.assertIsInstance(obj.name, str)
        self.assertIsInstance(obj.my_number, int)

        my_model_json = obj.to_dict()
        my_new_obj = User(**my_model_json)
        self.assertIsInstance(my_new_obj, User)
        self.assertTrue(my_new_obj is not obj)
        self.assertTrue(my_new_obj.created_at == obj.created_at)

        my_model_json["updated_at"] = 'toto'
        my_new_obj1 = User(**my_model_json)
        self.assertIsInstance(my_new_obj1.updated_at, datetime)

    def test_02__str__(self):
        """Test __str__ method"""
        obj = User()
        expected_str = "[User] ({}) {}".format(obj.id, obj.__dict__)
        self.assertTrue(str(obj) == expected_str)

    def test_03_save(self):
        """Test for save method"""
        if os.path.exists('file.json'):
            os.remove('file.json')
        obj = User()
        old_updated_at = obj.updated_at
        self.assertEqual(obj.created_at, obj.updated_at)

        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)
        self.assertTrue(obj.updated_at != old_updated_at)
        self.assertTrue(os.path.exists('file.json'))

    def test_04_to_dict(self):
        """Test to_dict method"""
        obj = User()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIsInstance(obj_dict["__class__"], str)
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)
        self.assertEqual(obj_dict["__class__"], "User")
        self.assertTrue(obj_dict["created_at"] == obj.created_at.isoformat())
        self.assertTrue(obj_dict["updated_at"] == obj.updated_at.isoformat())

    def test_05_attrs(self):
        """Test case for 'User' class attributes"""
        obj = User()
        self.assertEqual(obj.first_name, "")

    def test_06_inheritance(self):
        """Test case for 'User' class inheritance"""
        obj = User()
        self.assertIsInstance(obj, User)
        self.assertTrue(issubclass(type(obj), User))

    def test_07_instance(self):
        """Test case for 'User' class instance"""
        obj = User()
        self.assertIsInstance(obj, User)
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertTrue(hasattr(obj, "email"))
        self.assertTrue(hasattr(obj, "password"))
        self.assertTrue(hasattr(obj, "first_name"))
        self.assertTrue(hasattr(obj, "last_name"))
        self.assertFalse(hasattr(obj, "my_number"))
        obj.my_number = 89
        self.assertTrue(hasattr(obj, "my_number"))

    def test_08_docstring(self):
        """Test case for 'User' class docstring"""
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)
        self.assertIsNotNone(User.__str__.__doc__)
        self.assertIsNotNone(User.save.__doc__)
        self.assertIsNotNone(User.to_dict.__doc__)

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.userInstance = User()
        try:
            os.rename("file.json", "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """Class method to close test's environment"""
        try:
            os.remove("file.json")
            os.rename("test_file.json", "file.json")
        except Exception:
            pass

    def test_attrs(self):
        """Test case for 'User' class attributes"""
        self.assertEqual(self.userInstance.email, "")
        self.assertEqual(self.userInstance.password, "")
        self.assertEqual(self.userInstance.first_name, "")
        self.assertEqual(self.userInstance.last_name, "")

    def test_inheritance(self):
        """Test case for 'User' class inheritance"""
        self.assertIsInstance(self.userInstance, User)
        self.assertTrue(issubclass(type(self.userInstance), User))

    def test_instance(self):
        """Test case for 'User' class instance"""
        self.assertIsInstance(self.userInstance, User)  # instance
        self.assertTrue(hasattr(self.userInstance, "email"))
        self.assertTrue(hasattr(self.userInstance, "password"))
        self.assertTrue(hasattr(self.userInstance, "first_name"))
        self.assertTrue(hasattr(self.userInstance, "last_name"))

    def test_docstring(self):
        """Test case for 'User' class docstring"""
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)
        self.assertIsNotNone(User.__str__.__doc__)
        self.assertIsNotNone(User.save.__doc__)
        self.assertIsNotNone(User.to_dict.__doc__)

    def test_save(self):
        """Test case for 'User' class save method"""
        self.userInstance.save()
        self.assertNotEqual(self.userInstance.created_at,
                            self.userInstance.updated_at)

        user = User()
        old_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(old_updated_at, user.updated_at)

    def test_to_dict(self):
        """Test case for 'User' class to_dict method"""
        user_dict = self.userInstance.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["created_at"],
                         self.userInstance.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"],
                         self.userInstance.updated_at.isoformat())

        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["created_at"], user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"], user.updated_at.isoformat())

    def test_str(self):
        """Test case for 'User' class __str__ method"""
        string = "[User] ({}) {}".format(self.userInstance.id,
                                         self.userInstance.__dict__)
        self.assertEqual(string, str(self.userInstance))

    def test_attributes(self):
        """Test that User has the expected attributes."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attribute_types(self):
        """Test that User attributes are of the correct type."""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_attribute_defaults(self):
        """Test that User attributes are set to default values."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == "__main__":
    unittest.main()
