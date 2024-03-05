#!/usr/bin/python3
"""Unittest for User class"""
import unittest
import os
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class"""

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

    def test_str(self):
        """Test that the str method produces the correct string."""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))

    def test_save(self):
        """Test that the save method produces an updated 'updated_at'."""
        user = User()
        old_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(old_updated_at, user.updated_at)

    def test_to_dict(self):
        """Test that the to_dict method produces the correct dictionary."""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["created_at"], user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"], user.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
